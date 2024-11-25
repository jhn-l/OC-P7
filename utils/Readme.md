# Script : Téléchargement des Artefacts avec MLFlow

## 📋 **Description**
Ce script est conçu pour télécharger les derniers artefacts (modèle et vectorizer) enregistrés dans MLFlow. Il est principalement utilisé dans un contexte de gestion d’expérimentation pour centraliser et synchroniser les modèles et ressources nécessaires à une API ou une application d’analyse de sentiment.

---

## 🗂 **Fonctionnalités**
1. **Configuration de MLFlow** :
   - Définit l’URI de tracking de MLFlow : `http://mlflow-server:5000`.

2. **Initialisation des Artefacts** :
   - Deux artefacts sont ciblés :
     - Modèle : `RegLog_tfidf_lemmatize`.
     - Vectorizer associé : `RegLog_tfidf_lemmatize_vectorizer`.

3. **Gestion du Stockage** :
   - Les artefacts téléchargés sont stockés dans un dossier local nommé `artifacts`.
   - Le dossier est créé automatiquement s’il n’existe pas.

4. **Téléchargement des Artefacts** :
   - Utilise la méthode `MlflowClient.search_model_versions` pour lister toutes les versions disponibles d’un modèle donné.
   - Identifie la dernière version d’un artefact basé sur son ID de version.
   - Télécharge les artefacts via `mlflow.artifacts.download_artifacts` directement dans le dossier défini.

---
