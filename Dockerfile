FROM python:3.10-slim

WORKDIR /mlflow/mlflow-data

RUN python -m pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN echo $BACKEND_STORE_URI

CMD mlflow server --port $PORT --host 0.0.0.0 --backend-store-uri $BACKEND_STORE_URI