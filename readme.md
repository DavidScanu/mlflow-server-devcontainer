<img src="https://uploads-ssl.webflow.com/6108e07db6795265f203a636/61f90cbb8c06383f8944720e_ML%20Flow.png" width="600px" style="padding-bottom: 12px;">

# Lancer un serveur MLflow dans un codespace GitHub

Vous trouverez dans ce dépôt, tous les éléments nécessaires pour démarrer un [serveur MLflow](https://mlflow.org/docs/latest/tracking/tutorials/remote-server.html) dans un [codespace](https://docs.github.com/fr/codespaces/overview) GitHub (un serveur distant accessible depuis un notebook Google Colab).

Optionnellement, vous avez la possibilité d'utiliser ce dépôt pour lancer un serveur MLflow en local.

## A propos de MLflow

[MLflow](https://mlflow.org/docs/latest/introduction/index.html) fournit une suite d'outils visant à simplifier le flux de travail ML. Il est conçu pour aider les développeurs tout au long des différentes étapes de développement et de déploiement du ML. Les fonctionnalités principales de MLflow  sont :

- **Tracking**: MLflow Tracking fournit à la fois une API et une interface utilisateur dédiées à la journalisation des paramètres, des versions de code, des métriques et des artefacts pendant le processus ML.
- **Model Registry**: Une approche systématique de la gestion des modèles, aidant à gérer différentes versions de modèles et assurant une production fluide.
- **MLflow Deployments for LLMs**: Un serveur équipé d'API standardisées pour un accès simplifié aux modèles SaaS et OSS LLM.
- **Evaluate**: Outils conçus pour une analyse et une comparaison approfondies des modèles.
- **Prompt Engineering UI**: Outils conçus pour une analyse et une comparaison approfondies des modèles.
- **Recipes**: Lignes directrices pour structurer les projets ML, visant à garantir des résultats optimisés pour des scénarios de déploiement réels.
- **Projects**: Standardisez l'empaquetage du code ML, des flux de travail et des artefacts, en définissant les dépendances et les méthodes d'exécution pour chaque projet.

## TODO

### Création du fichier `devcontainer.json`

1. Installer environnement ubuntu et python (https://docs.github.com/fr/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers)
2. Installer extensions : python, docker, git
3. Set le thème de VSCode en dark par défaut
4. Installer les bibliothèques `pip install mlflow psycopg2 boto3`
5. Lancer `docker compose up -d`
6. Automatically forwarding a port (https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace#automatically-forwarding-a-port)
7. Lancer le automatiquement navigateur sur l'URL fowardée (pour afficher l'UI Mlflow)

### Misc

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

#### Utiliser le serveur MLflow depuis votre environnement distant

Pour utiliser le serveur MLflow depuis un **environnement distant** (ex: Colab, VM ou depuis votre PC), il faut définir l'**URI de tracking MLflow** en utilisant l'une de ces deux méthodes :

- Python : `mlflow.set_tracking_uri("http://url-public-exposee-par-codespace-github")`
- Variable d'environnement : `export MLFLOW_TRACKING_URI=http://url-public-exposee-par-codespace-github`

#### Démo

- Copier ce notebook Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1kfeJkVBVEAmaY1-84BOylGPZnDAV6C-v/view?usp=sharing)
- Changer la variable `mlflow_tracking_uri`
- Changer la variable `run_id`

### Alternative : Créer un serveur local

1. Cloner ce dépôt `git clone <URL>`
2. Lancer le conteneur du serveur MLflow : `docker compose up -d`
3. Accéder à l'interface utilisateur en accédant à `http://127.0.0.1:5001` dans votre navigateur.

#### Utiliser le serveur MLflow depuis votre environnement local

Alternativement, pour utiliser le serveur dans un **environnement local** (c-à-d dans le codespace lui-même), utiliser l'une de ces deux méthodes :
- Python : `mlflow.set_tracking_uri("http://127.0.0.1:5001")`
- Variable d'environnement : `export MLFLOW_TRACKING_URI=http://127.0.0.1:5001`

### Entraîner et tracker un modèle

Executer ce code python dans un notebook local ou notebook Colab, en remplaçant `mlflow_tracking_uri` par l'URI de Tracking MLflow qui convient.

```
# Check MLflow Tracking with simple training example
import mlflowExecuter ce code python dans un notebook local ou notebook Colab, en remplaçant `mlflow_tracking_uri` par l'URI de Tracking MLflow qui convient.

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

Exécuter ce code python dans un notebook local ou notebook Colab, en remplaçant :
- `mlflow_tracking_uri` par l'URI de Tracking MLflow qui convient.
- `run_id` par l'ID du run du modèle que vous souhaitez utiliser.

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

## A Propos

**David Scanu**, étudiant en Intelligence artificielle à l'école **Microsoft IA par Simplon et ISEN**.

<a href="https://www.linkedin.com/in/davidscanu14/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" ></a>
