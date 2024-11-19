
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

_💡 Illustration suggérée : Un schéma de pipeline pour le modèle classique._

---

### **Modèle Avancé (🔮 Techniques modernes)**

Pour améliorer la précision, des techniques plus complexes ont été explorées :

1. **Embeddings de mots** : 
   - Modèles utilisés : Word2Vec, FastText, GloVe.
   - Intégration dans des modèles Deep Learning avec des couches LSTM, capturant les relations contextuelles.

2. **BERT (✨)** :
   - Fine-tuning d’un modèle préentraîné pour la classification.
   - Utilisation de _Hugging Face_ et de _TensorFlow_ pour intégrer les embeddings de phrases.

_💡 Illustration suggérée : Comparaison des performances entre les modèles avancés et classiques (tableau ou courbe)._

---

### **Comparaison des Modèles 📈**

Les modèles ont été évalués sur des métriques pertinentes :
- **AUC (Area Under Curve)**.
- **Matrice de confusion** pour analyser les faux positifs et les faux négatifs.
- **Temps d’entraînement** et d’inférence.

_💡 Illustration suggérée : Matrice de confusion ou courbe ROC pour le meilleur modèle._

---

## **🛠️ Principes de MLOps**

Pour garantir l’industrialisation du projet, une démarche MLOps complète a été adoptée.

### Suivi des Expérimentations avec MLFlow

- **Tracking** : Historisation des hyperparamètres, des scores et des courbes ROC.
- **Gestion des modèles** : Enregistrement centralisé des artefacts, facilitant le déploiement et la comparaison des versions.

_💡 Illustration suggérée : Capture d’écran de l’interface MLFlow._

---

### API Flask pour le Déploiement 🌐

Une API a été développée pour exposer les prédictions du modèle en temps réel :
- Endpoint `/predict` : Recevant un tweet et retournant le sentiment associé.
- Tests unitaires pour valider la robustesse de l’API avant déploiement.

_💡 Illustration suggérée : Exemple de réponse JSON de l’API._

---

### Monitoring en Production 📡

- Utilisation d’Azure Application Insights pour capturer les erreurs et analyser les performances en conditions réelles.
- Logs et alertes configurés pour garantir une fiabilité continue.

---

## **📊 Résultats et Impact**

### Performances des Modèles

1. **Modèle classique** :
   - Simple mais limité en capacité de généralisation.

2. **Modèle avancé (LSTM)** :
   - Meilleures performances grâce à l’intégration des embeddings de mots.

3. **Modèle BERT** :
   - Résultats supérieurs, avec une meilleure capacité à comprendre les subtilités linguistiques.

---

### Résultats Clés ✅

- Le modèle BERT fine-tuné a atteint des scores d’AUC proches de 0,9 sur le jeu de test.
- La classification binaire a permis d’obtenir un équilibre parfait entre les classes, minimisant les biais.

_💡 Illustration suggérée : Tableau comparatif des métriques des trois modèles._

---

## **⚠️ Défis Rencontrés**

- **Problèmes de données** : Absence de tweets neutres, nécessitant une simplification à deux classes.
- **Optimisation des hyperparamètres** : Ajustement pour réduire le temps d’entraînement tout en maintenant des performances élevées.

---

## **🔮 Perspectives**

1. **Amélioration des Modèles** :
   - Intégrer des données supplémentaires pour inclure une classe neutre.
   - Explorer des architectures plus légères pour des prédictions en temps réel.

2. **Automatisation** :
   - Mise en place d’un pipeline CI/CD complet pour déployer rapidement les mises à jour du modèle.

3. **Analyse en Production** :
   - Exploiter les métriques capturées dans Application Insights pour améliorer continuellement les performances du modèle.

---

## **📌 Conclusion**

Ce projet a démontré comment des technologies de pointe et une approche MLOps peuvent transformer une problématique métier complexe en une solution pratique et efficace. Avec le modèle BERT, _Air Paradis_ est désormais mieux équipée pour anticiper les crises et préserver sa réputation en ligne.

---

## **🤝 À Vous de Contribuer !**

L’intégralité du code, des notebooks et des configurations est disponible sur GitHub. Testez les modèles, enrichissez les données, et aidez-nous à faire évoluer cette solution ! 🚀
