<img src="https://uploads-ssl.webflow.com/6108e07db6795265f203a636/61f90cbb8c06383f8944720e_ML%20Flow.png" width="600px" style="padding-bottom: 12px;">

# Lancer un serveur MLflow dans un Dev Container

Vous trouverez dans ce dépôt, tous les éléments nécessaires pour démarrer un [serveur MLflow](https://mlflow.org/docs/latest/tracking/tutorials/remote-server.html) dans un [Dev Container](https://containers.dev/). 

Vous pouvez lancer ce conteneur : 
- **en local sur votre machine** : en clonant ce dépôt et en lançant un Dev Container avec VS Code et Docker,
- **à distance depuis un [codespace](https://docs.github.com/fr/codespaces/overview) GitHub** : en lançant ce dépôt avec codespace.


## TODO

- Port Forwarding : 5001 et localhost 
- Base de donnée Postgresql
- Artefact Store
- Où stocker les variables d'environnement pour Artefact store et Database ?
- Merger tutorial.ipynb, train.py et try-model.py dans un Colab (https://drive.google.com/file/d/1kfeJkVBVEAmaY1-84BOylGPZnDAV6C-v/view?usp=sharing)

## A propos de MLflow

[MLflow](https://mlflow.org/docs/latest/introduction/index.html) fournit une suite d'outils visant à simplifier le flux de travail ML. Il est conçu pour aider les développeurs tout au long des différentes étapes de développement et de déploiement du ML. Les fonctionnalités principales de MLflow  sont :

- **Tracking**: MLflow Tracking fournit à la fois une API et une interface utilisateur dédiées à la journalisation des paramètres, des versions de code, des métriques et des artefacts pendant le processus ML.
- **Model Registry**: Une approche systématique de la gestion des modèles, aidant à gérer différentes versions de modèles et assurant une production fluide.
- **MLflow Deployments for LLMs**: Un serveur équipé d'API standardisées pour un accès simplifié aux modèles SaaS et OSS LLM.
- **Evaluate**: Outils conçus pour une analyse et une comparaison approfondies des modèles.
- **Prompt Engineering UI**: Outils conçus pour une analyse et une comparaison approfondies des modèles.
- **Recipes**: Lignes directrices pour structurer les projets ML, visant à garantir des résultats optimisés pour des scénarios de déploiement réels.
- **Projects**: Standardisez l'empaquetage du code ML, des flux de travail et des artefacts, en définissant les dépendances et les méthodes d'exécution pour chaque projet.
 

## Installation

### Créer un serveur MLflow dans codespace (serveur distant) 

1. **Créer un nouveau codespace** à partir de ce dépôt (UI de GitHub: Code / Codespaces / +)
2. **Accéder à l'UI MLflow** en accédant à l'**URL public exposée par codespace**. Dans le Terminal, onglet "Ports", définir l'URL du **port 5001** comme **public**.
3. **Utiliser cette URL** pour le tracking de vos travaux de machine learning, ou que vous soyez (Colab, Notebook, VM, un autre codespapce, etc...)

### Créer un serveur local

1. Cloner ce dépôt `git clone https://github.com/DavidScanu/mlflow-server.git` dans un dossier sur votre machine
2. Se déplacer à l'intérieur du dépôt GitHub : `cd mlflow-server/`
3. Dans VS Code, ouvrir la palette de commande (Ctrl+Alt+P) et chercher **Dev Containers: Reopen in container**.
4. Accéder à l'interface utilisateur en accédant à `http://localhost:5001` ou `http://127.0.0.1:5001` dans votre navigateur.

## Démonstration

Pour vérifier que le serveur MLflow est bien lancé et fonctionnel, exécuter le code python disponible dans le dossier `/demo` :

1. **Entrainer un modèle** : `python3 demo/train.py`. Vous devez voir apparaître un nouveau run dans l'UI MLflow et dans le Terminal.
2. **Copier le numéro de Run** (Run ID).
3. **Utiliser un modèle** : `python3 demo/try-model.py`. Entrez le numero de Run (Run ID) dans le Terminal. Cette commande retourne un modèle dans le Terminal.

## Guide d'utilisation

### Utilisation du serveur MLflow distant lancé dans codespace

Pour utiliser le serveur distant MLflow depuis un notebook Colab, VM ou depuis votre PC, il faut définir l'**URI de tracking MLflow** en utilisant l'une de ces deux méthodes :

- Python : `mlflow.set_tracking_uri("http://url-public-exposee-par-codespace-github")`
- Variable d'environnement : `export MLFLOW_TRACKING_URI=http://url-public-exposee-par-codespace-github`

Voici un exemple : 

- Copier ce notebook Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1kfeJkVBVEAmaY1-84BOylGPZnDAV6C-v/view?usp=sharing)
- Changer la variable `mlflow_tracking_uri`
- Changer la variable `run_id`

### Utiliser le serveur MLflow local

1. Créer un environnement python : `python3 -m venv .venv`
2. Activer l'environnement python : `source .venv/bin/activate`
3. Installer les bibliothèques python : `pip install mlflow psycopg2-binary boto3 scikit-learn==1.2.2`

Pour utiliser le serveur dans un **environnement local**, utiliser l'une de ces deux méthodes :

- Dans le code Python : `mlflow.set_tracking_uri("http://127.0.0.1:5001")` ou `mlflow.set_tracking_uri("http://localhost:5001")`
- Définir une variable d'environnement : `export MLFLOW_TRACKING_URI=http://127.0.0.1:5001` ou `export MLFLOW_TRACKING_URI=http://localhost:5001`

## Entraîner et tracker un modèle

Exécuter ce code python dans un notebook local ou notebook Colab, en remplaçant `mlflow_tracking_uri` par l'URI de Tracking MLflow qui convient.

```
# Check MLflow Tracking with simple training example
import mlflowExecuter ce code python dans un notebook local ou notebook Colab, en remplaçant `mlflow_tracking_uri` par l'URI de Tracking MLflow qui convient.

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor

# Remote server URIs
# mlflow_tracking_uri = "http://url-public-exposee-par-codespace-github"

# Local server URIs
mlflow_tracking_uri = "http://127.0.0.1:5001"

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

## Utiliser le modèle

Exécuter ce code python dans un notebook local ou notebook Colab, en remplaçant :
- `mlflow_tracking_uri` par l'URI de Tracking MLflow qui convient.
- `run_id` par l'ID du run du modèle que vous souhaitez utiliser.

```
import mlflow

# Remote server URIs
# mlflow_tracking_uri = "http://url-public-exposee-par-codespace-github"

# Local server URIs
mlflow_tracking_uri = "http://127.0.0.1:5001"

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
