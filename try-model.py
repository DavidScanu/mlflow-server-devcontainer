import mlflow

# Set local server URIs (Both URI seems to work)
mlflow_tracking_uri = "http://127.0.0.1:5001"
# mlflow_tracking_uri = "http://0.0.0.0:5001"

mlflow.set_tracking_uri(mlflow_tracking_uri)

run_id = "d323fb373cfa434ea8d5ecdfd80464f8"  # You can find run ID in the Tracking UI
artifact_path = "model"

# Download artifact via the tracking server
mlflow_artifact_uri = f"runs:/{run_id}/{artifact_path}"
local_path = mlflow.artifacts.download_artifacts(mlflow_artifact_uri)

# Load the model
model = mlflow.sklearn.load_model(local_path)

# If the model prints, everything works!
print(model)