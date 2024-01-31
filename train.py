# Check MLflow Tracking with simple training example
import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

# Set local server URIs (Both URI seems to work)
mlflow_tracking_uri = "http://127.0.0.1:5001"
# mlflow_tracking_uri = "http://0.0.0.0:5001"

mlflow.set_tracking_uri(mlflow_tracking_uri)

mlflow.autolog()

db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# Create and train models.
rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
rf.fit(X_train, y_train)

# Use the model to make predictions on the test dataset.
predictions = rf.predict(X_test)
