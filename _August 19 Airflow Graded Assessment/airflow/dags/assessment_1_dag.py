from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import os
import json

# File paths for intermediate storage
EXTRACT_PATH = "/tmp/extracted_data.json"
TRANSFORM_PATH = "/tmp/transformed_data.json"

# Task 1: Extract data
def extract_data():
    data = [
        {"id": 1, "name": "Elakkiya", "sales": 100},
        {"id": 2, "name": "Harish", "sales": 150},
        {"id": 3, "name": "Kashifa", "sales": 200}
    ]
    with open(EXTRACT_PATH, 'w') as f:
        json.dump(data, f)
    print(f"Data extracted and saved to {EXTRACT_PATH}")

# Task 2: Transform data
def transform_data():
    if os.path.exists(EXTRACT_PATH):
        with open(EXTRACT_PATH, 'r') as f:
            data = json.load(f)
        # Add 10% commission to sales
        for row in data:
            row["commission"] = row["sales"] * 0.1
        with open(TRANSFORM_PATH, 'w') as f:
            json.dump(data, f)
        print(f"Data transformed and saved to {TRANSFORM_PATH}")
    else:
        raise FileNotFoundError(f"{EXTRACT_PATH} not found")

# Task 3: Load data
def load_data():
    if os.path.exists(TRANSFORM_PATH):
        with open(TRANSFORM_PATH, 'r') as f:
            data = json.load(f)
        for row in data:
            print(f"Loading row: {row}")
        print("Data load simulation complete.")
    else:
        raise FileNotFoundError(f"{TRANSFORM_PATH} not found")

# Define the DAG
with DAG(
    dag_id="assessment_1_dag",
    start_date=datetime(2025, 8, 19),
    schedule_interval=None,
    catchup=False,
    tags=["etl", "assignment"]
) as dag:

    # Step 1: Extract
    extract_task = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data
    )

    # Step 2: Transform
    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data
    )

    # Step 3: Load
    load_task = BashOperator(
        task_id="load_data",
        bash_command=f"python3 -c 'import json; f=open(\"{TRANSFORM_PATH}\"); data=json.load(f); print(\"Loaded rows:\", len(data)); f.close()'"
    )

    # Set task order
    extract_task >> transform_task >> load_task