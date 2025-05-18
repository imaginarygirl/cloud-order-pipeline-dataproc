# Cloud Order Pipeline (GCP - Dataproc, BigQuery, Composer)

This project simulates a batch data pipeline for processing order transactions using Google Cloud Platform tools. It reflects a real-world use case of ingesting, transforming, and analyzing data using scalable cloud-native services.

## Tech Stack

- **Google Cloud Storage (GCS)** – Raw data storage (CSV files)
- **Dataproc (PySpark)** – Batch transformation and cleaning
- **BigQuery** – Data warehouse and final output storage
- **Cloud Composer (Airflow)** – Workflow orchestration

## Pipeline Flow

1. Ingest raw CSV data into GCS
2. Trigger Dataproc job to clean and transform data
3. Load processed data into BigQuery
4. Orchestrate with Composer (DAG to manage the steps)
5. (Optional) Simulate CR handling and business validation as post-processing

## Folder Structure

cloud-order-pipeline-dataproc/
├── data/ # Sample input data
├── dataproc_jobs/ # PySpark transformation scripts
├── sql/ # BigQuery table schema and queries
├── dags/ # Cloud Composer DAGs
├── notebooks/ # Exploration & testing notebooks
├── docs/ # Architecture diagram and documentation
└── README.md # Project description


## Author

Camila M. Martins  
[LinkedIn](https://www.linkedin.com/in/camila-martins-532193b0/)
