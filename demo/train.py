import mlflow
from mlflow.models import infer_signature
from mlflow import MlflowClient

import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Dummy machine learning training

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "multi_class": "auto",
    "random_state": 8888,
}

# Train the model
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)

# Predict on the test set
y_pred = lr.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)



# MLFlow Tracking

def print_logged_info(r):
    print("")
    print("⚗️ MLflow Run Infos :")
    tags = {k: v for k, v in r.data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in MlflowClient().list_artifacts(r.info.run_id, "model")]
    print(f"🏃 run_id: {r.info.run_id}")
    print(f"⚡ artifacts: {artifacts}")
    print(f"⚙️ params: {r.data.params}")
    print(f"📝 metrics: {r.data.metrics}")
    print(f"🏷️ tags: {tags}")
    print()

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://localhost:5001")

# Create a new MLflow Experiment
mlflow.set_experiment("Demo Codespace")

# Start an MLflow run
with mlflow.start_run() as run:
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the loss metric
    mlflow.log_metric("accuracy", accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Demo", "Basic LR model for iris data")

    # Infer the model signature
    signature = infer_signature(X_train, lr.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=lr,
        artifact_path="model",
        signature=signature,
        input_example=X_train
        # registered_model_name="tracking-quickstart",
    )

# fetch the auto logged parameters and metrics for ended run
print_logged_info(mlflow.get_run(run_id=run.info.run_id))