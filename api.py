from flask import Flask, request, jsonify
from transformers import BertTokenizer
import tensorflow as tf
import mlflow
import mlflow.pyfunc
import os

# Remplacer 'runs:/<run_id>/bert_model' par l'URI de votre modèle BERT loggé dans MLflow
logged_model_uri = 'runs:/459dc97ed043438cb8acadc62d5dc92a/bert_model'

# Télécharger l'artefact du modèle et l'enregistrer dans un dossier local
local_model_path = mlflow.artifacts.download_artifacts(logged_model_uri)


# Charger le tokenizer BERT (assurez-vous qu'il correspond au modèle entraîné)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')


# Charger le modèle Keras depuis le fichier local
local_model_file = os.path.join(local_model_path, 'data', 'model.keras')
loaded_model = tf.keras.models.load_model(local_model_file)
# Charger le modèle BERT entraîné depuis MLflow
loaded_model = mlflow.keras.load_model(local_model_file)

# Initialiser l'application Flask
app = Flask(__name__)

# Définir un point d'entrée pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données envoyées dans la requête
        data = request.get_json()

        # Vérifier que le champ "text" est présent
        if "text" not in data:
            return jsonify({'error': 'Le champ "text" est manquant dans la requête'}), 400

        # Tokenizer le texte
        text_data = data["text"]
        tokens = tokenizer(
            text_data, max_length=128, padding=True, truncation=True, return_tensors='tf'
        )

        # Prédire avec le modèle chargé
        logits = loaded_model(tokens['input_ids'], attention_mask=tokens['attention_mask']).logits
        predictions = tf.argmax(logits, axis=1).numpy()

        # Retourner les prédictions en format JSON
        return jsonify({'predictions': predictions.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Lancer l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8123)
