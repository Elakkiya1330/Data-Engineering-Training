from pathlib import Path
import pandas as pd
import numpy as np
import os
from azure.storage.blob import BlobServiceClient, ContentSettings

# paths
INPUT_FILE = "data/sales_data.csv"
RAW_OUT = "output/raw_sales_data.csv"
PROC_OUT = "output/processed_sales_data.csv"

def clean_and_enrich():
    df_raw = pd.read_csv(INPUT_FILE)

    # make sure output folder exists
    Path("output").mkdir(exist_ok=True)

    # save raw
    df_raw.to_csv(RAW_OUT, index=False)

    # process
    df = df_raw.copy()
    df = df.drop_duplicates(subset=["order_id"], keep="first")
    df["region"] = df["region"].fillna("Unknown")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)
    df["cost"] = pd.to_numeric(df["cost"], errors="coerce").fillna(0)

    df["profit_margin"] = np.where(df["revenue"] > 0,(df["revenue"] - df["cost"]) / df["revenue"],0)

    def segment(r):
        if r > 100000:
            return "Platinum"
        elif r > 50000:
            return "Gold"
        return "Standard"

    df["customer_segment"] = df["revenue"].apply(segment)

    df.to_csv(PROC_OUT, index=False)
    print("Processed file saved.")

def upload_to_blob(file_path):
    account = os.getenv("AZURE_STORAGE_ACCOUNT_NAME")
    key = os.getenv("AZURE_STORAGE_ACCOUNT_KEY")
    container = os.getenv("AZURE_CONTAINER_NAME")

    conn_str = f"DefaultEndpointsProtocol=https;AccountName={account};AccountKey={key};EndpointSuffix=core.windows.net"
    blob_service = BlobServiceClient.from_connection_string(conn_str)
    container_client = blob_service.get_container_client(container)

    with open(file_path, "rb") as f:
        container_client.upload_blob(
            name=Path(file_path).name,
            data=f,
            overwrite=True,
            content_settings=ContentSettings(content_type="text/csv")
        )
    print(f"Uploaded {file_path} to container {container}.")

if __name__ == "__main__":
    clean_and_enrich()
    upload_to_blob(RAW_OUT)
    upload_to_blob(PROC_OUT)

