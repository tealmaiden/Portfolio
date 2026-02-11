
import asyncio
import csv
from playwright.async_api import async_playwright
from datetime import datetime

CSV_FILE = "tradesmith_positions.csv"
LOG_FILE = "scrape_log.txt"
POSITIONS_URL = "https://finance.tradesmith.com/portfolios/positions"

async def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now().isoformat()} - {msg}\n")

async def extract_all_positions():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(POSITIONS_URL)
        await log("Waiting for user to select portfolio...")
        print("🕒 Waiting 100 seconds for portfolio selection...")
        await page.wait_for_timeout(100000)

        await page.wait_for_selector("tr.app-table__tr")
        rows = await page.query_selector_all("tr.app-table__tr")
        positions_meta = []

        for row in rows:
            try:
                link = await row.query_selector('a[href*="/position-details/"]')
                if not link:
                    continue
                url = await link.get_attribute("href")
                if not url:
                    continue
                full_url = url if url.startswith("http") else f"https://finance.tradesmith.com{url}"
                ticker = await link.inner_text()

                entry_date = ""
                exit_date = ""
                valid_dates = []

                date_divs = await row.query_selector_all('div[title]')
                for div in date_divs:
                    title = await div.get_attribute("title")
                    if title and "/" in title and len(title) >= 8:
                        try:
                            parsed_date = datetime.strptime(title.strip(), "%m/%d/%Y")
                            valid_dates.append((parsed_date, title.strip()))
                        except ValueError:
                            continue

                if valid_dates:
                    valid_dates.sort()
                    entry_date = valid_dates[0][1]
                    if len(valid_dates) > 1:
                        exit_date = valid_dates[-1][1]

                long_short_cell = await row.query_selector('td div[title="Long"], td div[title="Short"]')
                long_short = await long_short_cell.inner_text() if long_short_cell else ""

                positions_meta.append({
                    "Ticker": ticker,
                    "Entry Date": entry_date,
                    "Exit Date": exit_date,
                    "L/S": long_short,
                    "Edit URL": full_url
                })
            except Exception as e:
                await log(f"⚠️ Failed reading table row: {e}")
                continue

        await log(f"Collected {len(positions_meta)} rows from main table.")

        # Visit each details page
        import random
        detailed_positions = []
        for i, pos in enumerate(positions_meta):
            if i > 0 and i % 15 == 0:
                await log(f"⏳ Sleeping after {i} rows to avoid rate limiting...")
                await asyncio.sleep(random.uniform(60, 90))
            try:
                await page.goto(pos["Edit URL"])
                await page.wait_for_selector('button:has(svg use[href="#edit"])', timeout=15000)
                await page.click('button:has(svg use[href="#edit"])')
                await asyncio.sleep(2)
                await page.wait_for_selector('.details-entry-price-item__input', timeout=15000)

                entry_input = await page.query_selector('.details-entry-price-item__input')
                entry_price = await entry_input.get_attribute("value") if entry_input else ""
                entry_price = entry_price.replace("$", "").replace(",", "").strip() if entry_price else ""

                # Try to locate exit price by label
                all_inputs = await page.query_selector_all("input")
                exit_price = ""
                for input_el in all_inputs:
                    parent = await input_el.evaluate_handle('el => el.closest("div")')
                    label_text = await page.evaluate('(el) => el?.previousElementSibling?.innerText', parent)
                    if label_text and "Exit Price" in label_text:
                        exit_price = await input_el.get_attribute("value")
                        break

                if not exit_price:
                    await log(f"❌ Exit Price not found for {pos['Edit URL']}")
                else:
                    await log(f"✅ Exit Price for {pos['Ticker']}: {exit_price}")

                shares_input = await page.query_selector(".details-number-item__input")
                shares = await shares_input.get_attribute("value") if shares_input else ""
                shares = shares.replace(",", "").strip() if shares else ""
                exit_price = exit_price.replace("$", "").replace(",", "").strip() if exit_price else ""

                detailed_positions.append({
                    **pos,
                    "Shares": shares,
                    "Entry Price": entry_price,
                    "Exit Price": exit_price
                })
            except Exception as e:
                await log(f"⚠️ Failed navigating to edit page for {pos['Ticker']}: {e}")
                continue

        await log(f"✅ Collected {len(detailed_positions)} complete positions. Saving to CSV...")

        with open(CSV_FILE, "w", newline="") as csvfile:
            fieldnames = ["Ticker", "Entry Date", "Exit Date", "L/S", "Shares", "Entry Price", "Exit Price", "Edit URL"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(detailed_positions)

        await log("✅ Done.")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(extract_all_positions())
