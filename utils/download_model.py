"""
Script : Téléchargement des Artefacts avec MLFlow

Description :
Ce script est conçu pour télécharger les derniers artefacts (modèle et vectorizer)
enregistrés dans MLFlow. Il est principalement utilisé pour centraliser et synchroniser
les modèles nécessaires à une API ou une application d’analyse de sentiment.
"""



import mlflow
from mlflow.tracking import MlflowClient
import os

# Configuration MLflow
mlflow.set_tracking_uri("http://mlflow-server:5000")

# Nom des artefacts
model_name = "RegLog_tfidf_lemmatize"
vectorizer_name = f"{model_name}_vectorizer"

# Dossier où les artefacts seront stockés
output_dir = "artifacts"
os.makedirs(output_dir, exist_ok=True)

# Initialiser le client MLflow
client = MlflowClient()

def download_latest_artifact(model_name, output_dir):
    """
    Télécharge le dernier modèle ou vectorizer depuis MLFlow et le sauvegarde dans le dossier spécifié.

    Arguments :
    - model_name (str) : Nom du modèle à télécharger.
    - output_dir (str) : Chemin du dossier de stockage des artefacts.

    Exceptions :
    - ValueError : Si aucune version du modèle n'est trouvée.
    """
    # Récupérer les versions disponibles dans le registre
    all_versions = client.search_model_versions(f"name='{model_name}'")
    if not all_versions:
        raise ValueError(f"Aucune version du modèle '{model_name}' n'a été trouvée dans MLflow.")

    # Sélectionner la dernière version
    latest_version = max(all_versions, key=lambda x: int(x.version))
    run_id = latest_version.run_id

    # Construire l'URI et télécharger l'artefact directement dans output_dir
    model_uri = f"runs:/{run_id}/{model_name}"
    local_path = mlflow.artifacts.download_artifacts(model_uri, dst_path=output_dir)
    print(f"Artefact '{model_name}' téléchargé et sauvegardé dans : {local_path}")

# Télécharger et enregistrer le modèle
download_latest_artifact(model_name, output_dir)

# Télécharger et enregistrer le vectorizer
download_latest_artifact(vectorizer_name, output_dir)
