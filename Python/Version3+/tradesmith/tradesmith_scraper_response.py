## Key Mapping Help:
# import json

# with open("rows.txt", "r") as f:
#     data = json.load(f)

# rows = data.get("gridRows", [])

# if not rows:
#     print("No rows found.")
# else:
#     print("First row preview:")
#     for k, v in rows[0].items():
#         print(f"{k}: {v}")


import json
import csv
from datetime import datetime

INPUT_FILE = "rows.txt"
OUTPUT_FILE = "tradesmith_positions_from_api.csv"

def parse_date(date_str):
    if not date_str:
        return ""
    return date_str.split("T")[0]

with open(INPUT_FILE, "r") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError as e:
        print("❌ JSON decode error:", e)
        exit()

print("Top-level keys:", list(data.keys()) if isinstance(data, dict) else type(data))

rows = data.get("gridRows", [])

if not rows:
    print("No rows found.")
    exit()

extracted = []

for row in rows:
    try:
        extracted.append({
            "Ticker": row.get("symbol", ""),
            "Symbol Name": row.get("symbolName", ""),
            "Entry Date": parse_date(row.get("purchaseDate", "")),
            "Exit Date": parse_date(row.get("closeDate", "")),
            "Entry Price": row.get("purchasePriceAdj", ""),
            "Exit Price": row.get("closePrice", ""),
            "Shares": row.get("shares", ""),
            "L/S": ("Long" if str(row.get("tradeType", "")) == "1" else "Short" if str(row.get("tradeType", "")) == "2" else row.get("tradeType", "")),  # Map "1"->Long, "2"->Short
            "Notes": row.get("notes", ""),
            "Tags": ", ".join(row.get("tags", [])) if isinstance(row.get("tags", []), list) else row.get("tags", ""),
            "Portfolio": row.get("portfolioName", "")
        })
    except Exception as e:
        print(f"⚠️ Error parsing row: {e}")

# Save to CSV
with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=extracted[0].keys())
    writer.writeheader()
    writer.writerows(extracted)

print(f"✅ Extracted {len(extracted)} rows to {OUTPUT_FILE}")
