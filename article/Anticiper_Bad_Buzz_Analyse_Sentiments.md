
# 🌟 **Anticiper les Bad Buzz grâce à l’Analyse de Sentiments avec Deep Learning** 🌟

Dans un monde où la réputation en ligne est cruciale, les entreprises doivent anticiper les bad buzz sur les réseaux sociaux. 
Ce projet, réalisé pour la compagnie aérienne _Air Paradis_, vise à développer un prototype d’intelligence artificielle capable de prédire 
les sentiments associés à des tweets. Découvrez comment les approches classiques et avancées du Deep Learning, combinées aux principes 
du MLOps, ont permis de relever ce défi ambitieux. 🚀

---

## **📖 Contexte et Objectif**

_Air Paradis_, confrontée à des critiques régulières sur les réseaux sociaux, a sollicité une solution capable de détecter rapidement 
les tweets négatifs. L’objectif était de concevoir un modèle d’analyse de sentiments prédisant si un tweet est **positif** ou **négatif**, 
à partir de données publiques issues de Twitter.

### Les Données 📊

- **Dataset utilisé** : Sentiment140 contenant 1,6 million de tweets, répartis en deux classes : négative (0) et positive (4).
- **Problème binaire** : Le dataset ne contenait pas de tweets neutres, simplifiant la tâche à une classification binaire.

---

## **🔍 Approches et Méthodologie**

### **Modèle Classique (🎩 Baseline)**

La première étape consistait à développer une solution simple et robuste :

- **Algorithme** : Régression logistique.
- **Vectorisation** : TF-IDF et CountVectorizer.
- **Prétraitement** : Suppression des doublons, lemmatisation et stemming.
- **Résultats** : Un modèle baseline permettant d’obtenir une première évaluation des performances sur un sous-ensemble de 20 000 tweets.

### **Modèle Avancé (🔮 Techniques modernes)**

Pour améliorer la précision, des techniques plus complexes ont été explorées :

1. **Embeddings de mots** : 
   - Modèles utilisés : Word2Vec, FastText, GloVe.
   - Intégration dans des modèles Deep Learning avec des couches LSTM, capturant les relations contextuelles.

2. **BERT (✨)** :
   - Fine-tuning d’un modèle préentraîné pour la classification.
   - Utilisation de _Hugging Face_ et de _TensorFlow_ pour intégrer les embeddings de phrases.

---

## **🛠️ Principes de MLOps**

### Suivi des Expérimentations avec MLFlow

- **Tracking** : Historisation des hyperparamètres, des scores et des courbes ROC.
- **Gestion des modèles** : Enregistrement centralisé des artefacts, facilitant le déploiement et la comparaison des versions.

### **ML, DEV et OPS dans un pipeline MLOps**

![Pipeline MLOps](image-mlops.webp)
*source: https://www.phdata.io/blog/mlops-vs-devops-whats-the-difference/*

L'image ci-dessous illustre un pipeline MLOps, combinant les pratiques de Machine Learning (ML), Développement (DEV), et Opérations (OPS) pour garantir une mise en production efficace et une gestion continue des modèles d'apprentissage automatique.

- **ML (Machine Learning)** : Cette phase se concentre sur la préparation des données et le développement des modèles. Elle comprend la collecte, le nettoyage, et la transformation des données, suivis de l'entraînement, la validation, et l'optimisation des modèles. Ces étapes sont cruciales pour construire des modèles performants capables de prédire les sentiments avec précision.
- **DEV (Développement)** : Une fois le modèle ML prêt, il est intégré dans une application ou un service. Cette phase couvre la planification, le packaging, et les tests pour s'assurer que le modèle peut être utilisé dans un environnement de production. Cela inclut la création d'API (comme celles développées dans ce projet) pour exposer le modèle de manière accessible.
- **OPS (Opérations)** : Cette dernière phase garantit le déploiement et le suivi des performances en production. Elle inclut des étapes comme la configuration des pipelines, le monitoring des métriques (par exemple via MLflow ou Azure Application Insights), et l'implémentation de processus de gestion des alertes et des versions pour maintenir les modèles à jour et performants.

Ce schéma met en évidence l'interconnexion entre ces trois domaines pour assurer une livraison fluide et itérative des solutions d'IA, tout en minimisant les risques opérationnels.

| **Outil**         | **Phase MLOps** | **Rôle principal**                                                                                     | **Description**                                                                                         |
|--------------------|-----------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Git**           | DEV, OPS        | Gestion des versions                                                                                   | Permet de versionner le code, les notebooks, et les fichiers de configuration pour collaborer efficacement. |
| **GitHub Actions**| OPS             | Automatisation des pipelines CI/CD                                                                     | Exécute automatiquement des workflows pour tester, valider, et déployer les modèles ou applications.    |
| **Docker**        | DEV, OPS        | Conteneurisation pour la reproductibilité et le déploiement                                            | Standardise les environnements en encapsulant le code, les dépendances, et les configurations dans des conteneurs. |
| **MLflow**        | ML, OPS         | Suivi des expérimentations, gestion et déploiement des modèles                                         | Enregistre les paramètres, métriques, et artefacts. Facilite le suivi des modèles et leur déploiement en production. |

