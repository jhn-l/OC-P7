from flask import Flask, request, jsonify
import mlflow
from mlflow.tracking import MlflowClient
from mlflow import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os
import tensorflow as tf

#import os
#os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
mlflow.set_tracking_uri("http://mlflow-server:5000") 

# Initialiser l'application Flask
app = Flask(__name__)

# Initialiser le client MLflow
client = MlflowClient()

# Lister les modèles enregistrés pour vérifier l'accès au registre
client = MlflowClient()

print("Vérification des modèles disponibles dans le registre MLflow :")
for registered_model in client.search_registered_models():
    print(f"Nom du modèle : {registered_model.name}")
    for version in registered_model.latest_versions:
        print(f" - Version : {version.version}, Run ID : {version.run_id}, Status : {version.status}")


# Nom du modèle dans le registre MLflow
model_name = "RegLog_tfidf_lemmatize"

# Récupérer toutes les versions du modèle et trouver la plus récente
all_versions = client.search_model_versions(f"name='{model_name}'")

# Vérifier s'il y a des versions disponibles
if all_versions:
    # Trouver la version la plus récente du modèle
    latest_version = max(all_versions, key=lambda x: int(x.version))
    run_id = latest_version.run_id

    # Construire le chemin local vers le modèle en utilisant le run_id et le nom de l'artifact
    local_model_path = f"/tmp/mlruns/1/{run_id}/artifacts/{model_name}"
    
    # Charger le modèle Keras depuis le chemin local sans téléchargement
    loaded_model =sklearn.load_model(local_model_path)
    print(f"Modèle chargé avec succès depuis le chemin local : {local_model_path}")
else:
    raise ValueError(f"Aucune version du modèle '{model_name}' n'a été trouvée dans MLflow.")

vectorizer_name = f"{model_name}_vectorizer"  # Assumant que le vectorizer est enregistré avec un suffixe
# Récupérer la dernière version du vectorizer
all_versions_vectorizer = client.search_model_versions(f"name='{vectorizer_name}'")
if all_versions_vectorizer:
    latest_version_vectorizer = max(all_versions_vectorizer, key=lambda x: int(x.version))
    run_id_vectorizer = latest_version_vectorizer.run_id
    vectorizer_uri = f"runs:/{run_id_vectorizer}/{vectorizer_name}"
    tfidf_vectorizer = sklearn.load_model(vectorizer_uri)
    print(f"Vectorizer TF-IDF chargé avec succès depuis : {vectorizer_uri}")
else:
    raise ValueError(f"Aucune version du vectorizer '{vectorizer_name}' n'a été trouvée dans MLflow.")


# Définir un point d'entrée pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées dans la requête
        data = request.get_json()

        # Vérifier que le champ "text" est présent
        if "text" not in data:
            return jsonify({'error': 'Le champ "text" est manquant dans la requête'}), 400

        # Récupérer le texte
        text_data = data["text"]

        # Transformer le texte en vecteurs TF-IDF
        X_transformed = tfidf_vectorizer.transform([text_data])

        # Prédire avec le modèle chargé
        predictions = loaded_model.predict(X_transformed)

        # Retourner les prédictions en format JSON
        return jsonify({'predictions': predictions.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Lancer l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8123)
    
