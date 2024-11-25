
# Analyse de Sentiments avec Deep Learning

## 📋 **Introduction**
Ce projet a pour objectif de développer un prototype d'IA capable d'anticiper les bad buzz sur les réseaux sociaux pour la compagnie aérienne _Air Paradis_. En analysant les tweets, le modèle prédit si la phrase est **positive** ou **négative**. Ce projet inclut des méthodologies classiques et avancées, avec une orientation MLOps pour le suivi et le déploiement en production.

---

## 🗂 **Structure des Fichiers**
- `api.py` : Code Flask pour exposer le modèle sous forme d'API.
- `utils/download_model.py` : Script pour télécharger les artefacts depuis MLFlow.
- `tests/test-unit-api.py` : Tests unitaires pour vérifier les fonctionnalités de l'API.
- `DockerfileAPI` & `docker-compose.yml` : Configuration pour la containerisation et le déploiement sur le cloud via `unit_test_api.yml`.
- `notebooks/` : 
  - **1-modele-classique.ipynb** : Modèle classique basé sur régression logistique (testés sur 20 000 tweets).
  - **2-modele-avance-BERT.ipynb** : Modèle de Word embeddings et LSTM, utilisation également de modèle pré-entrainés (testés sur 20 000 tweets).
  - **3-modele-BERT.ypnb** : Entrainement d'un modèle BERT et essais de fine tuning (testés sur 1 000 tweets).
- `artifacts/utils/download_model.py` : Contient les modèles et vectorizers téléchargés depuis MLFlow à l'aide du script.
- `README.md` : Documentation du projet.
- `article/README_Analyse_Sentiments.md` : Article sur l'évaluation et le résultat de plusieurs modèles d'analyses de sentiments obtenus grâce aux différents notebooks.

---

## 🚀 **Technologies Utilisées**
- **Frameworks et Bibliothèques** :
  - Flask : Pour exposer le modèle en API.
  - TensorFlow/Keras : Développement des modèles avancés.
  - Scikit-learn : Modèle classique et vectorisation.
  - MLFlow : Suivi des expérimentations et gestion des artefacts.
- **MLOps** :
  - Azure Application Insights : Suivi des performances en production.
- **Containerisation** :
  - Docker et Docker Compose.

---

## 🛠 **Instructions pour Exécuter le Projet**

### **Prérequis**
1. Build les images Docker pour  le fichier `docker-compose.yml` :
   ```bash
   docker compose build
   ```
2. Lancer les images Docker:
   ```bash
   docker compose up -d
   ```
3. Pour le suivi des expérimentations MLFlow:
   ```bash
   http://localhost:5000
   ```

### **Exécution en Local**
1. **API** :
   - Démarrer l'API Flask :
     ```bash
     python api.py
     ```
   - Tester une prédiction :
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "Je suis heureux"}' http://127.0.0.1:8000/predict
     ```

2. **Tests unitaires** :
   - Exécuter les tests unitaires :
     ```bash
     pytest test-unit-api.py
     ```

3. **Interface** :
   - Interface locale pour tester les prédictions dans un Notebook `interface-api.ipynb`.

---

## 📊 **Approches Modélisées**

### Modèle Classique
- Algorithme : Régression Logistique.
- Vectorisation : TF-IDF / CountVectorizer avec lemmatization et stemming. 

### Modèles Avancés
- Embeddings avec ['w2v', 'fasttext', 'bert', 'use'] + Régression Logistique
- LSTM avec embeddings Word2Vec et FastText.
- Différent modèles BERT (pré-entrainé et entrainé) pour un meilleur contexte sémantique.

### Méthodologies MLOps
- **Tracking avec MLFlow** :
  - Suivi des expérimentations : Accuracy, AUC, hyperparamètres, temps d'entraînement.
  - Centralisation des artefacts et des modèles.
- **Déploiement** :
  - Pipeline CI/CD avec tests unitaires automatiques et mise en production via GitHub Actions.

---

## 🧪 **Tests et Validation**
- **Tests unitaires** :
  - Vérification du chargement du modèle.
  - Tests de prédictions valides pour des tweets positifs et négatifs.
  - Code coverage inclus dans le github `Actions`.

---

## 🌐 **Déploiement en Production**
- Déploiement via Docker sur le cloud Azure.
- Suivi des erreurs et alertes grâce à Azure Application Insights :
  - Traces des tweets mal classifiés.
  - Alerte déclenchée après 3 erreurs en moins de 5 minutes.

---

## 👨‍💻 **Contributeurs**
- **Nom** : Lévêque
- **Prénom** : Jonathan
- **Email** : jon.leveque@gmail.com

---

En cas de problème, n'hésitez pas à créer une issue ou à me contacter directement.
