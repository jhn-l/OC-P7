import pytest
from flask import Flask
from api import app, loaded_model, tfidf_vectorizer  # Importer les objets directement

# Utiliser le client de test de Flask pour simuler des requêtes à l'API
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test pour vérifier que le modèle et le vectorizer sont bien chargés
def test_model_and_vectorizer_loaded():
    assert loaded_model is not None, "Le modèle n'a pas été chargé correctement dans l'API."
    assert tfidf_vectorizer is not None, "Le vectorizer n'a pas été chargé correctement dans l'API."

# Test pour vérifier que l'API retourne une prédiction valide pour un texte positif
def test_predict_positive(client):
    response = client.post('/predict', json={'text': 'Je suis tellement heureux aujourd\'hui!'})
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'predictions' in json_data
    assert isinstance(json_data['predictions'], list)  # Vérifie que les prédictions sont sous forme de liste

# Test pour vérifier que l'API retourne une prédiction valide pour un texte négatif
def test_predict_negative(client):
    response = client.post('/predict', json={'text': 'Je suis très triste et déçu.'})
    json_data = response.get_json()
    assert response.status_code == 200
    assert 'predictions' in json_data
    assert isinstance(json_data['predictions'], list)

# Test pour vérifier que l'API retourne une erreur si le champ "text" est manquant
def test_missing_text_field(client):
    response = client.post('/predict', json={})
    json_data = response.get_json()
    assert response.status_code == 400
    assert 'error' in json_data
    assert json_data['error'] == 'Le champ "text" est manquant dans la requête'
