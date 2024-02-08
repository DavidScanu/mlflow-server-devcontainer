import mlflow

# Set local server URIs
mlflow_tracking_uri = "http://localhost:5001"
# mlflow_tracking_uri = "http://127.0.0.1:5001"
# mlflow_tracking_uri = "http://0.0.0.0:5001"

mlflow.set_tracking_uri(mlflow_tracking_uri)

# Prompts user with the Run ID from MLflow run
# You can find run ID in the Tracking UI
while True:
    run_id = input('Please enter your RUN ID : ')
    if run_id.strip() != '':
        break

artifact_path = "model"

# Download artifact via the tracking server
mlflow_artifact_uri = f"runs:/{run_id}/{artifact_path}"

try: 
    local_path = mlflow.artifacts.download_artifacts(mlflow_artifact_uri)
    # Load the model
    model = mlflow.sklearn.load_model(local_path)

    # Load the model back for predictions as a generic Python Function model
    # loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)

    # If the model prints, everything works!
    print(f"🤖 Model : {model}")
except:
  print("❌ Invalid Run ID.")


# https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html