# Car Valuation IA - Marché Tunisien 🚗

Ce projet est une application de Machine Learning capable de prédire le prix des véhicules en utilisant un algorithme de Régression (Random Forest). L'interface permet une estimation adaptée au marché tunisien grâce à un ajustement des taxes et du taux de change.

## 📊 Performance du Modèle
- **Précision (R2 Score) :** 95.43%
- **Erreur Moyenne (MAE) :** 1315.33 (DT)
- **Algorithme :** RandomForestRegressor (Scikit-Learn)

## 🛠️ Technologies utilisées
- **Langage :** Python 3.x
- **Librairies Data :** Pandas, NumPy, Scikit-Learn, Joblib
- **Interface :** Streamlit
- **Environnement :** Jupyter Notebook (Analyse & Entraînement)

## 📁 Structure du Projet
- `notebooks/` : Contient les étapes d'exploration, nettoyage et entraînement.
- `models/` : Contient le modèle sérialisé (`.pkl`) et la liste des colonnes.
- `app.py` : Code source de l'application web interactive.
- `data/` : Dossier contenant le dataset original et traité.

## 🚀 Installation et Lancement

1. **Cloner le projet**
```bash
git clone [https://github.com/votre-utilisateur/tunisian-car-valuation.git](https://github.com/votre-utilisateur/tunisian-car-valuation.git)
cd tunisian-car-valuation
Installer les dépendances

Bash
pip install streamlit pandas scikit-learn joblib
Lancer l'application

Bash
streamlit run app.py
💡 Fonctionnalités
Saisie interactive de 9 caractéristiques techniques (puissance, poids, moteur...).

Traitement automatique des variables catégoriques (One-Hot Encoding).

Conversion dynamique vers le prix du marché tunisien (Coefficient x3.5).

Affichage du prix en Dinars Tunisiens (DT) et en Dollars ($).

📝 Auteur
Ahmed Baccari - https://github.com/Ahmed37012


   