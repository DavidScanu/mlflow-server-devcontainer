FROM python:3.10-slim

WORKDIR /mlflow-data

COPY requirements.txt .

RUN pip install psycopg2-binary boto3 mlflow

CMD mlflow server --port $PORT --host 0.0.0.0