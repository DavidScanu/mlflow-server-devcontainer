<img src="https://uploads-ssl.webflow.com/6108e07db6795265f203a636/61f90cbb8c06383f8944720e_ML%20Flow.png" width="600px" style="padding-bottom: 12px;">

# Lancer un serveur MLflow dans un codespace GitHub

Vous trouverez dans ce dépôt, tous les éléments nécessaires pour démarrer un serveur MLflow dans un codespace GitHub (un serveur distant accessible depuis un notebook Google Colab). En option, vous avez la possibilité d'utiliser ce dépôt pour lancer un serveur MLflow en local.

## TODO

- Create `devcontainer.json`

1. Installer environnement ubuntu et python (https://docs.github.com/fr/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
2. Installer les bibiolthèques `pip install mlflow psycopg2 boto3`
3. Installer extensions : python, docker,
4. 4. Lancer `docker compose up -d`
5. Automatically forwarding a port (https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace#automatically-forwarding-a-port)
6. Lancer le automatiquement navigateur sur l'URL fowardée (pour afficher l'UI Mlflow)

- renommer le dépôt GitHub
- Add "mlruns/" à `.gitignore`
- Mettre les fichiers train.py et try-model.py dans un dossier "demo"
- Merger tutorial.ipynb, train.py et try-model.py dans un Colab (https://drive.google.com/file/d/1kfeJkVBVEAmaY1-84BOylGPZnDAV6C-v/view?usp=sharing)
- Add Postegresql database
- Add artefact store
- Ou stocker les variables d'environnement pour Artefact store et Database ?

## Guide d'utilisation

### Créer un serveur MLflow dans codespace (remote server) 

1. Créer un codespace à partir de ce dépôt (UI de GitHub: Code / Codespaces / +)
2. Installer les bibliothèques python : `pip install mlflow psycopg2 boto3` (à enlever)
3. Lancer le conteneur du serveur MLflow : `docker compose up -d` (à enlever)
4. Accéder à l'interface utilisateur en accédant à l'URL public exposée par codespace. Dans le Terminal, cliquer sur "Ports", puis définir l'URL du port 5001 comme public.

### Créer un serveur local (alternative)

1. Cloner ce dépôt `git clone <URL>`
2. Lancer le conteneur du serveur MLflow : `docker compose up -d`
3. Accéder à l'interface utilisateur en accédant à `http://127.0.0.1:5001` dans votre navigateur.

### Utiliser le serveur MLflow depuis votre environnement distant

Pour utiliser le serveur MLflow depuis votre environnement de développement, il faut définir l'**URI de tracking MLflow**.

Pour utiliser le serveur MLflow depuis un **environnement distant** (ex: Colab, VM ou en local sur votre PC), utiliser l'une de ces deux méthodes :
- Python : `mlflow.set_tracking_uri("http://url-public-exposee-par-codespace-github")`
- Variable d'environnement : `export MLFLOW_TRACKING_URI=http://url-public-exposee-par-codespace-github`

#### Démo

- Copier ce notebook Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1kfeJkVBVEAmaY1-84BOylGPZnDAV6C-v/view?usp=sharing)
- Changer la variable `mlflow_tracking_uri`
- Changer la variable `run_id`

### Utiliser le serveur MLflow depuis votre environnement local (dans le codespace)

Alternativement, pour utiliser le serveur dans un **environnement local** (c-à-d dans le codespace lui-même), utiliser l'une de ces deux méthodes :
- Python : `mlflow.set_tracking_uri("http://127.0.0.1:5001")`
- Variable d'environnement : `export MLFLOW_TRACKING_URI=http://127.0.0.1:5001`

### Entraîner et tracker un modèle

Executer ce code dans un notebook local ou notebook Colab, en remplaçant `mlflow_tracking_uri` par l'URI de Tracking MLflow qui convient.

```
# Check MLflow Tracking with simple training example
import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

# Remote server URIs
mlflow_tracking_uri = "http://url-public-exposee-par-codespace-github"

# Local server URIs
# mlflow_tracking_uri = "http://127.0.0.1:5001"

# Set MLflow Tracking URI
mlflow.set_tracking_uri(mlflow_tracking_uri)

mlflow.autolog()

db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# Create and train models.
rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
rf.fit(X_train, y_train)

# Use the model to make predictions on the test dataset.
predictions = rf.predict(X_test)
```

### Utiliser un modèle

```
import mlflow

# Remote server URIs
mlflow_tracking_uri = "http://url-public-exposee-par-codespace-github"

# Local server URIs
# mlflow_tracking_uri = "http://127.0.0.1:5001"

# Set MLflow Tracking URI
mlflow.set_tracking_uri(mlflow_tracking_uri)

run_id = "YOUR_RUN_ID"  # You can find run ID in the Tracking UI
artifact_path = "model"

# Download artifact via the tracking server
mlflow_artifact_uri = f"runs:/{run_id}/{artifact_path}"
local_path = mlflow.artifacts.download_artifacts(mlflow_artifact_uri)

# Load the model
model = mlflow.sklearn.load_model(local_path)

# If the model prints, everything works!
print(model)
```

## Docker Hub

- <a href="https://hub.docker.com/r/davidscanu/mlflow-server" target="_BLANK">https://hub.docker.com/r/davidscanu/mlflow-server</a>

## Créer une image Docker personnalisée

Utiliser le `Dockerfile` pour créer votre propre image personnalisée avec la commande :
`docker build -t nom-de-l-image .`

## A Propos

**David Scanu**, étudiant en Intelligence artificielle à l'école **Microsoft IA par Simplon et ISEN**.

<a href="https://www.linkedin.com/in/davidscanu14/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" ></a>
