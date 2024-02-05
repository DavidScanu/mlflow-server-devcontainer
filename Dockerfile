FROM python:3.10-slim

WORKDIR /mlflow-data

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY demo ./demo

CMD mlflow server --port $PORT --host 127.0.0.1