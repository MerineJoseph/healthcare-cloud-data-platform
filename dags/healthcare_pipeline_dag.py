from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "etl"))

from pipeline import run_pipeline


default_args = {
    "owner": "data_engineering",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


with DAG(
    dag_id="healthcare_etl_pipeline",
    default_args=default_args,
    description="ETL pipeline for healthcare operational analytics data",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["healthcare", "etl", "data-engineering"],
) as dag:

    run_healthcare_pipeline = PythonOperator(
        task_id="run_healthcare_pipeline",
        python_callable=run_pipeline,
    )

    run_healthcare_pipeline
