from flask import Flask, request, jsonify
import pickle
import os
from mlflow import sklearn

# Dossier contenant les artefacts pour la production
artifact_dir = "artifacts"
model_name = "RegLog_tfidf_lemmatize"
vectorizer_name = f"{model_name}_vectorizer"

# Variables globales pour le modèle et le vectorizer
loaded_model = None
tfidf_vectorizer = None


# Initialiser l'application Flask
app = Flask(__name__)

def load_artifacts():
    """Charge le modèle et le vectorizer depuis les fichiers locaux."""
    try:
        # Charger le modèle
        model_path = os.path.join(artifact_dir, model_name)
        loaded_model = sklearn.load_model(model_path)
        print(f"Modèle chargé avec succès depuis : {model_path}")

        # Charger le vectorizer
        vectorizer_path = os.path.join(artifact_dir, vectorizer_name, "model.pkl")
        with open(vectorizer_path, 'rb') as f:
            tfidf_vectorizer = pickle.load(f)
        print(f"Vectorizer TF-IDF chargé avec succès depuis : {vectorizer_path}")

        return loaded_model, tfidf_vectorizer

    except Exception as e:
        print(f"Erreur lors du chargement des artefacts : {e}")
        return None, None

# Charger les artefacts au démarrage de l'application
loaded_model, tfidf_vectorizer = load_artifacts()

# Définir un point d'entrée pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    # Vérifier que le modèle et le vectorizer sont chargés
    if loaded_model is None or tfidf_vectorizer is None:
        return jsonify({'error': 'Le modèle ou le vectorizer n\'a pas pu être chargé pour la prédiction'}), 500

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
