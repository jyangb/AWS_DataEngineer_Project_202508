"""
Convert the UCI Online Retail Excel dataset to CSV format.
Input: raw_data/Online Retail.xlsx
Output: raw_data/online_retail.csv
"""

import pandas as pd
from pathlib import Path

RAW_DIR = Path("raw_data")

def convert_excel_to_csv():
    input_file = RAW_DIR / "Online Retail.xlsx"
    output_file = RAW_DIR / "online_retail.csv"

    df = pd.read_excel(input_file)
    df.to_csv(output_file, index=False)
    print(f"Saved CSV to {output_file}")

if __name__ == "__main__":
    convert_excel_to_csv()
