FROM python:3.10-slim

WORKDIR /mlflow/mlflow-data

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD mlflow server --port $PORT --host 0.0.0.0