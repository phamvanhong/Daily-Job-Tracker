import sys
sys.path.insert(0, '/opt/airflow/src/')
from hello_world import hello_world
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# Định nghĩa DAG
with DAG(
    dag_id="new_dag",
    start_date=datetime(2024, 1, 1),  # Ngày bắt đầu
    schedule_interval="@daily",      # Chạy hàng ngày
    catchup=False,                     # Không chạy lại các DAG cũ
) as dag:

    task_hello = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world
    )

    task_hello
