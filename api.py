from flask import Flask, request, jsonify
import pickle
import os
import logging
from mlflow import sklearn
from opencensus.ext.azure.log_exporter import AzureLogHandler 


# Traceur Azure Application Insights
# Votre clé d’instrumentation
INSTRUMENTATION_KEY = '2abd6f3d-5473-4b85-88d8-174a16dacf8a'


# Configuration du logger pour Application Insights
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(AzureLogHandler(connection_string=f'InstrumentationKey={INSTRUMENTATION_KEY}'))

# Fonction pour tester la configuration du logger
def test_logger_configuration(message="Test de configuration du logger"):
    logger.info(message)
    return "Log sent" 

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
        logger.error('Erreur de prédiction', exc_info=True)
        return jsonify({'error': str(e)}), 400


# Avec cette configuration :

# La route /feedback reçoit un feedback pour chaque prédiction, qu'elle soit correcte ou incorrecte.
# En cas de feedback négatif (non_valide), une trace de niveau warning est envoyée.
# En cas de feedback positif (valide), une trace de niveau info est envoyée.

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    if "text" not in data or "prediction" not in data or "feedback" not in data:
        return jsonify({'error': 'Requête invalide'}), 400
    
    tweet_text = data["text"]
    prediction_result = data["prediction"]
    feedback_type = data["feedback"]

    # Enregistrer le feedback dans Application Insights ou un autre système de suivi ici
    if feedback_type == "non_valide":
        logger.warning("Prédiction incorrecte", extra={
            "custom_dimensions": {
                "tweet": tweet_text,
                "prediction": prediction_result
            }
        })
    elif feedback_type == "valide":
        logger.info("Prédiction validée", extra={
            "custom_dimensions": {
                "tweet": tweet_text,
                "prediction": prediction_result
            }
        })

    return jsonify({'status': 'Feedback reçu'})

# Lancer l'application
if __name__ == '__main__':
    # Envoyer un log de test au démarrage pour vérifier la configuration
    test_logger_configuration("Démarrage de l'application - vérification du logger")
    app.run(host='0.0.0.0', port=8123)

