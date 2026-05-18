🤖 E2/E3 — Rapport Modèle IA + API IA
docs/E2_E3_report.md

1. Veille IA
Modèles testés : RandomForest, XGBoost, Logistic Regression

Choix : RandomForest (robuste, peu sensible au scaling)

2. Préparation des données
Sélection features

Encodage OneHot

Split train/test

3. Entraînement
Script : train.py  
Pipeline scikit‑learn :

OneHotEncoder

RandomForestClassifier

4. Évaluation
Accuracy : ~0.82

Rapport classification joint

5. API IA
Fichier : app/api_ia.py  
Endpoint :

POST /predict

6. Tests
tests/test_api_ia.py