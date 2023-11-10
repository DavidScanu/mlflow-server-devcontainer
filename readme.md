<img src="https://uploads-ssl.webflow.com/6108e07db6795265f203a636/61f90cbb8c06383f8944720e_ML%20Flow.png" >

# Serveur local MLFlow pour Machine Learning

## Docker Hub 

- <a href="https://hub.docker.com/r/davidscanu/mlflow-server" target="_BLANK">https://hub.docker.com/r/davidscanu/mlflow-server</a>

## How-to use

### Télécharger l'image du serveur MLFlow 

`docker pull davidscanu/mlflow-server`

### Lancer le serveur MLFlow dans un conteneur Docker 

`docker run -d --name mlflow-local-server -v $(pwd)/mlflow-data:/mlflow-data -p 5001:5001 -e PORT=5001 davidscanu/mlflow-server:v1.0`

### Se connecter au serveur à l'adresse suivante :
`http://localhost:5001`.

### Paramètres

- `-p 5001:5001` : changer le numéro de port en utilisant la structure suivante : `-p port-de-host:port-dans-le-container`.
- `-e PORT=5001` : port utilsé par le serveur MLFLow à l'intérieur du container.
- `--name mlflow-local-server` : changer le nom du container.
- `-v $(pwd)/mlflow-data:/mlflow-data` : les données des logs de MLFlow sont stockées dans un dossier `mlflow-data`. Ce flag permet de synchroniser ce dossier avec votre dossier local. 

## Créer une image Docker personnalisée

Utiliser le `Dockerfile` pour créer votre propre image personnalisée avec la commande :
`docker build -t nom-de-l-image .`.

## A Propos

**David Scanu**, étudiant en Intelligence artificielle à l'école **Microsoft IA par Simplon et ISEN**.

<a href="https://www.linkedin.com/in/davidscanu14/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" ></a>