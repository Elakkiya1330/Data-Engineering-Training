from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import json
import random

# Default DAG arguments
default_args = {
    'owner': 'elakkiya',
    'depends_on_past': False,
    'email': ['elakkiya913270@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# DAG definition
with DAG(
    dag_id='assessment_2_dag',
    default_args=default_args,
    description='A scheduled data audit DAG',
    schedule_interval='@hourly',
    start_date=datetime(2025, 8, 19),
    catchup=False
) as dag:

    # Task 1: Simulate data pull from external source
    def pull_data():
        data = {'record_count': random.randint(50, 150), 'last_updated': '2025-08-19T11:00:00'}
        return data

    task_pull_data = PythonOperator(
        task_id='pull_data',
        python_callable=pull_data
    )

    # Task 2: Audit rule validation
    def validate_audit(**context):
        data = context['ti'].xcom_pull(task_ids='pull_data')
        threshold = 100
        audit_passed = data['record_count'] <= threshold
        result = {
            'record_count': data['record_count'],
            'threshold': threshold,
            'status': 'PASS' if audit_passed else 'FAIL'
        }

        # Store audit result
        with open('/tmp/audit_result.json', 'w') as f:
            json.dump(result, f)

        if not audit_passed:
            raise ValueError(f"Audit failed: record_count {data['record_count']} exceeds threshold {threshold}")

        return result

    task_validate_audit = PythonOperator(
        task_id='validate_audit',
        python_callable=validate_audit,
        provide_context=True
    )

    # Task 3: Log audit results using Bash
    task_log_results = BashOperator(
        task_id='log_audit_results',
        bash_command='echo "Audit completed successfully. Check /tmp/audit_result.json for details."'
    )

    # Task 4: Final status update (PythonOperator)
    def final_status():
        with open('/tmp/audit_result.json', 'r') as f:
            result = json.load(f)
        print(f"Final audit status: {result['status']}")

    task_final_status = PythonOperator(
        task_id='final_status_update',
        python_callable=final_status
    )

    # DAG task dependencies
    task_pull_data >> task_validate_audit >> task_log_results >> task_final_status
