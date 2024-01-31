<img src="https://uploads-ssl.webflow.com/6108e07db6795265f203a636/61f90cbb8c06383f8944720e_ML%20Flow.png" width="600px" style="padding-bottom: 12px;">

# Serveur local MLFlow pour Machine Learning

## TODO

- Create `devcontainer.json`

Présentation des conteneurs de développement
https://docs.github.com/fr/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers

1. Installer environnement ubuntu et python
2. Installer les bibiolthèques `pip install mlflow psycopg2 boto3`
3. Installer extensions : python, docker, 
3. Automatically forwarding a port (https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace#automatically-forwarding-a-port)
4. Lancer `docker compose up -d`


- Vérifier train.py
- Vérifier tutorial.ipynb
- Tester avec Colab (https://drive.google.com/file/d/1kfeJkVBVEAmaY1-84BOylGPZnDAV6C-v/)
- Add Postegresql database
- Add artefact store
- Ou stocker les variables d'environnement pour Artefact store et Database ?

## Ressources utilisées

Remote Experiment Tracking with MLflow Tracking Server
- https://mlflow.org/docs/latest/tracking/tutorials/remote-server.html


## Guide d'utilisation

### Utiliser ce dépôt pour créer un serveur local

1. Cloner ce dépôt `git clone <URL>`
2. Lancer le serveur MLFlow : `docker compose up -d`
3. Accéder à l'interface utilisateur en accédant à `http://127.0.0.1:5000` dans votre navigateur
4. Définir l'**URI de tracking MLflow** :  
   - Option 1 : Dans le code python, `mlflow.set_tracking_uri("http://localhost:5001")` 
   - Option2 : Variable d'environnement, `export MLFLOW_TRACKING_URI=http://127.0.0.1:5000`

### Comment utiliser ce dépôt dans Codespaces

1. Créer un codespace à partir de ce dépôt (UI : Code / Codespaces / +)
2. Installer les bibliothèques python : `pip install mlflow psycopg2 boto3` (à enlever)
3. Démarrer les conteneurs avec la commande : `docker compose up -d` (à enlever)
4. Accéder à l'interface utilisateur en accédant à l'URL public exposée par codespace, en cliquant sur `http://127.0.0.1:5000` au lancement du serveur
5. Définir l'**URI de tracking MLflow**, en fonction de votre environnement de développement. Suivre le tableau suivant :  

| Environnement                      | Dans le code Python                                                                                                 | Configuration variable d'environnement                                                                                                         |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Le même codespace que le serveur | `mlflow.set_tracking_uri("http://localhost:5001")`        | `export MLFLOW_TRACKING_URI=http://127.0.0.1:5000`                                                                                           |
| Un notebook Colab            | `mlflow.set_tracking_uri("http://url-public-exposee-par-codespace-github")` |     "Secrets" (menu de gauche)<br>Nom : `MLFLOW_TRACKING_URI` </br>Valeur : `http://url-public-exposee-par-codespace-github`                                                                                                                                          |
| - En local <br>- Un autre codespace </br>- Une VM | `mlflow.set_tracking_uri("http://url-public-exposee-par-codespace-github")`                                   | `export MLFLOW_TRACKING_URI=http://url-public-exposee-par-codespace-github`                                                             |




## Docker Hub

- <a href="https://hub.docker.com/r/davidscanu/mlflow-server" target="_BLANK">https://hub.docker.com/r/davidscanu/mlflow-server</a>

## Créer une image Docker personnalisée

Utiliser le `Dockerfile` pour créer votre propre image personnalisée avec la commande :
`docker build -t nom-de-l-image .`

## A Propos

**David Scanu**, étudiant en Intelligence artificielle à l'école **Microsoft IA par Simplon et ISEN**.

<a href="https://www.linkedin.com/in/davidscanu14/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" ></a>