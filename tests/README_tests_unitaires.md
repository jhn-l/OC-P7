
# Tests Unitaires pour l'API Flask

## 📋 **Description**

Ce script contient des tests unitaires pour valider le fonctionnement de l'API Flask développée pour prédire les sentiments des tweets à l'aide d'un modèle de machine learning. Les tests couvrent plusieurs aspects, notamment :

- La vérification de la disponibilité des artefacts (modèle et vectorizer).
- La validation des prédictions.
- La gestion des erreurs et exceptions.
- Le comportement des points d'entrée `/predict` et `/feedback`.

---

## 🛠 **Structure des Tests**

### Tests de Base

1. **Chargement des Artefacts** :
   - Vérifie que le modèle et le vectorizer sont chargés correctement.
   - Simule des scénarios de succès et d'échec du chargement.

2. **Prédictions** :
   - Vérifie les réponses de l'API pour des prédictions valides (textes positifs et négatifs).
   - Gère les cas où :
     - Le champ `text` est manquant.
     - Le modèle ou le vectorizer n'est pas chargé.
     - Une exception se produit pendant la prédiction.

3. **Retour d'Informations via `/feedback`** :
   - Vérifie le traitement des retours utilisateur (feedback).
   - Simule des logs pour les cas de feedback valides et non valides.
   - Gère les erreurs dans les requêtes.

---

## 🚀 **Exécution des Tests**

### **Prérequis**

1. Installer les dépendances requises :

   ```bash
   pip install pytest flask
   ```

2. Assurez-vous que le fichier principal de l'API (`api.py`) et ses dépendances (modèle et vectorizer) sont accessibles.

### **Exécution des Tests**

Utilisez les commandes suivantes pour exécuter les tests :

1. **Lancer tous les tests** :

   ```bash
   pytest test_unit_api.py
   ```

2. **Tester uniquement les prédictions (`/predict`)** :

   ```bash
   pytest test_unit_api.py -k "predict"
   ```

3. **Tester uniquement le retour d'information (`/feedback`)** :

   ```bash
   pytest test_unit_api.py -k "feedback"
   ```

4. **Afficher un rapport détaillé** :
   ```bash
   pytest test_unit_api.py -v
   ```

5. **Générer un rapport de couverture du code** :

   ```bash
   pytest --cov=api test_unit_api.py
   ```

6. **Exécuter un test spécifique par son nom** :

   ```bash
   pytest test_unit_api.py -k "test_predict_positive"
   ```

---

## 🗂 **Structure des Fichiers**

- **`api.py`** : Le fichier principal de l'API Flask, contenant la logique pour `/predict` et `/feedback`.
- **`test_unit_api.py`** : Ce script, contenant les tests unitaires.
- **Artefacts** :
  - Modèle et vectorizer nécessaires pour les prédictions.

---

## 📑 **Détails des Tests**

### 1. Tests de Disponibilité des Artefacts

- **Objectif** : Vérifie que le modèle et le vectorizer sont bien chargés depuis les artefacts.
- **Scénarios** :
  - Succès : Les artefacts sont chargés correctement.
  - Échec : Une exception survient pendant le chargement.

### 2. Tests de Prédictions

- **Objectif** : Valider les réponses de l'API `/predict`.
- **Scénarios Couverts** :
  - Texte valide (positif ou négatif).
  - Champ `text` manquant dans la requête.
  - Modèle ou vectorizer non chargé.
  - Erreur pendant la transformation ou la prédiction.

### 3. Tests de Feedback

- **Objectif** : Vérifier le comportement de l'API `/feedback`.
- **Scénarios Couverts** :
  - Requête valide avec feedback positif ou négatif.
  - Requête invalide (champs manquants).
  - Vérification des logs dans les cas de feedback.

---

## 🌟 **Fonctionnalités Clés**

- **Simulation avec `pytest`** :
  - Utilise les fixtures pour initialiser un client Flask.
  - Simule des exceptions avec `monkeypatch`.

- **Couverture des Scénarios d'Erreur** :
  - Gestion des erreurs côté serveur.
  - Vérification de la robustesse des points d'entrée.

---

## 💡 **Exemples de Commandes**

Voici quelques exemples supplémentaires pour exécuter des tests spécifiques ou obtenir plus d'informations :

- Lancer uniquement les tests qui vérifient le chargement des artefacts :

  ```bash
  pytest test_unit_api.py -k "load_artifacts"
  ```

- Obtenir un rapport de couverture avec détails par fichier :

  ```bash
  pytest --cov=api --cov-report=term-missing test_unit_api.py
  ```

- Générer un rapport HTML de couverture :

  ```bash
  pytest --cov=api --cov-report=html test_unit_api.py
  ```

- Exécuter les tests avec une pause en cas d'échec (mode interactif) :

  ```bash
  pytest --pdb test_unit_api.py
  ```
