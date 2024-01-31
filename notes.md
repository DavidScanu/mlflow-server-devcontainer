#### Option 2 :

`docker build -t votre-nom/nom-de-l-image .`

`docker run -d --name mlflow-local-server -v $(pwd)/mlflow-data:/mlflow-data -p 5001:5001 -e PORT=5001 votre-nom/nom-de-l-image`

#### Explication des paramètre de la commande `docker run`

- `-p 5001:5001` : changer le numéro de port en utilisant la structure suivante : `-p port-de-host:port-dans-le-container`
- `-e PORT=5001` : port utilsé par le serveur MLFLow à l'intérieur du container
- `--name mlflow-local-server` : le nom du container
- `-v $(pwd)/mlflow-data:/mlflow-data` : les données des logs de MLFlow sont stockées dans un dossier `mlflow-data`. Ce flag permet de synchroniser ce dossier avec votre dossier local. 