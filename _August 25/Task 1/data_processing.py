import pandas as pd
from datetime import datetime

# File paths
RAW_FILE = "data/raw_sales_data.csv"
CLEAN_FILE = "data/clean_sales_data.csv"

def clean_data():
    # Read raw CSV
    df = pd.read_csv(RAW_FILE)

    # Drop rows with missing values
    df = df.dropna()

    # Normalize column names to lowercase
    df.columns = [col.strip().lower() for col in df.columns]

    # Convert date columns to YYYY-MM-DD (if any)
    for col in df.columns:
        if "date" in col:
            try:
                df[col] = pd.to_datetime(df[col]).dt.strftime("%Y-%m-%d")
            except Exception:
                pass  # skip if not convertible

    # Save cleaned file
    df.to_csv(CLEAN_FILE, index=False)

if __name__ == "__main__":
    clean_data()