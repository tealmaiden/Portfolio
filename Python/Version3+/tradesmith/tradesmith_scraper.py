import asyncio
import pandas as pd
from datetime import datetime

from bs4 import BeautifulSoup

def inspect_rows(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    all_trs = soup.find_all("tr")
    print(f"Found {len(all_trs)} <tr> elements.")

    if all_trs:
        print("✅ First <tr> element preview:")
        print(all_trs[0].prettify())

#Best way to extract data from the HTML file
# This function assumes the HTML file has been downloaded and saved locally
def extract_from_html(html_file_path, name):
    # Load and parse the downloaded HTML file
    print(f"🔍 Extracting data from {html_file_path}...")
    with open(html_file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Extract all <tr> elements (excluding header rows)
    rows = soup.select("table tr")
    data = []

    for row in rows:
        if row.find("th"):
            continue  # Skip header rows

        ticker_tag = row.select_one('a.table-cell-ticker-action__stock-symbol')
        shares_tag = row.select_one('td[data-column-name="Shares"]')
        entry_date_tag = row.select_one('td[data-column-name="EntryDate"]')
        exit_date_tag = row.select_one('td[data-column-name="ExitDate"]')
        entry_price_tag = row.select_one('td[data-column-name="EntryPrice"]')
        exit_price_tag = row.select_one('td[data-column-name="ExitPrice"]')
        commissions_tag = row.select_one('td[data-column-name="Commissions"]')
        total_cb_tag = row.select_one('td[data-column-name="TotalCB"]')
        ls_tag = row.select_one('td[data-column-name="LS"]')
        tags_tag = row.select_one('td[data-column-name="Tags"]')
        notes_tag = row.select_one('td[data-column-name="Notes"]')
        value_tag = row.select_one('td[data-column-name="Value"]')
        health_tag = row.select_one('td[data-column-name="Health"]')

        if not ticker_tag:
            continue  # skip rows without a ticker

        ticker = ticker_tag.get_text(strip=True)
        ticker_url = ticker_tag.get("href")

        shares = float(shares_tag.get("sortvalue", "0")) if shares_tag else None
        entry_date = entry_date_tag.get("title") if entry_date_tag else None
        exit_date = exit_date_tag.get("title") if exit_date_tag else None
        entry_price = entry_price_tag.get("sortvalue", "0") if entry_price_tag else None
        exit_price = exit_price_tag.get("sortvalue", "0") if exit_price_tag else None
        commissions = float(commissions_tag.get("sortvalue", "0")) if commissions_tag else None
        total_cb = float(total_cb_tag.get("sortvalue", "0")) if total_cb_tag else None
        long_short = ls_tag.get_text(strip=True) if ls_tag else None
        tags = tags_tag.get_text("sortvalue") if tags_tag else None
        notes = notes_tag.get_text("sortvalue") if notes_tag else None
        value = value_tag.get_text("sortvalue") if value_tag else None
        health = health_tag.get_text(strip=True) if health_tag else None

        #Updated columns names to match turbotax import
        data.append({
            "Currency Name": ticker,
            "URL": f"{ticker_url}/position-details" if ticker_url else None,
            "RawShares": shares, # keep original shares value, which can be negative for shorts
            "Shares": abs(shares) if shares is not None else None,  # Use absolute value for shares
            "Purchase Date": entry_date,
            "Date Sold": exit_date,
            "Entry Price": entry_price,
            "Exit Price": exit_price,
            "Commissions": commissions,
            "tradesmith Cost Basis (wrong for short trades)": total_cb,
            "L/S": long_short,
            "Tags": tags,
            "Notes": notes,
            "Value": value,
            "Health": health
        })

    if data:
        df = pd.DataFrame(data)
        df.to_csv(f"{name}.csv", index=False)
        print(f"✅ Saved {len(df)} rows to '{name}.csv'")
    else:
        print("❌ No valid rows parsed from HTML.")


if __name__ == "__main__":
    #asyncio.run(extract_positions())

    # For debugging, you can run the HTML extraction directly
    extract_from_html("TradeSmith Finance __ Positions.html", "open positions output")
    # Or inspect the rows in the HTML file
    #inspect_rows("debug_table.html")