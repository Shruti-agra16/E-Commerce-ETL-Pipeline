from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow/scripts')
from etl_logic import run_silver_layer, run_gold_layer

with DAG(
    dag_id='shruti_ecom_project',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False
) as dag:

    task_silver = PythonOperator(
        task_id='run_silver_cleaning',
        python_callable=run_silver_layer
    )

    task_gold = PythonOperator(
        task_id='run_gold_transformation',
        python_callable=run_gold_layer
    )

    # Dependency: Silver ke baad Gold
    task_silver >> task_gold