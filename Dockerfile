FROM apache/airflow:2.10.5-python3.12
COPY requirements.txt .
RUN pip install -r requirements.txt