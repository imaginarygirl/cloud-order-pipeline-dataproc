from airflow import models
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

PROJECT_ID = 'get-coordenates'
REGION = 'us-central1'  # e.g., 'europe-west1'
CLUSTER_NAME = 'order-pipeline-cluster'

# PySpark file in GCS
PYSPARK_URI = 'gs://order-pipeline-bucket-cm/scripts/transform_orders.py'

default_args = {
    'owner': 'camila',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with models.DAG(
    'order_pipeline_dataproc_dag',
    default_args=default_args,
    schedule_interval=None,  # Run on demand (you can set to '0 6 * * *' for daily at 6 AM)
    catchup=False,
) as dag:

    submit_dataproc_job = DataprocSubmitJobOperator(
        task_id='run_dataproc_transform',
        job={
            "reference": {"project_id": PROJECT_ID},
            "placement": {"cluster_name": CLUSTER_NAME},
            "pyspark_job": {"main_python_file_uri": PYSPARK_URI},
        },
        region=REGION,
        project_id=PROJECT_ID,
    )

    submit_dataproc_job
