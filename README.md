# 2026-03-17_projet_final_certification_devIA

projet_final/
│
├── README.md                    ← à rédiger en priorité
├── data/
│   ├── evenements.csv           ← données d'entraînement (60 lignes, "seed")
│   └── evenements_1500.csv      ← jeu de données étendu (1500 lignes)
├── notebooks/
│   ├── 01_exploration.ipynb     ← EDA (à créer si pas fait)
│   ├── 02_modelisation.ipynb    ← votre notebook "La finale.ipynb" renommé
│   └── 03_streamlit_dev.ipynb   ← votre notebook Streamlit
├── app/
│   └── app.py                   ← votre application Streamlit
├── models/
│   └── (modèle sérialisé joblib ou pickle — voir phase 3)
└── docs/
    └── (présentation, rapport, etc.)

L'objectif de ce projet final est de démontrer votre capacité à mener un projet de data science de bout en bout, en intégrant les différentes compétences acquises au cours de la formation. Vous devrez explorer et analyser les données, construire et évaluer un modèle de machine learning, puis déployer une application interactive avec Streamlit pour présenter vos résultats. 

# Projet DevIA — Certification 2026

**Auteur**: ValentinPhan  
**But**: Démontrer les compétences DevIA (collecte, intégration IA, application) pour la certification.

## Structure du dépôt
- data/ : jeux `evenements.csv`, `evenements_1500.csv`
- notebooks/ : 01_exploration.ipynb, 02_modelisation.ipynb, 03_streamlit_dev.ipynb
- app/ : app.py (Streamlit)
- models/ : modèles sérialisés
- docs/ : documentation, rapports, openapi.yaml

## Prérequis
- Python 3.10+, pip
- PostgreSQL (ou SQLite pour dev)
- Docker (optionnel)
- Outils recommandés: DVC, MLflow, GitHub Actions

## Installation rapide (dev)
1. `git clone <repo>`
2. `python -m venv .venv && source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. Charger les données : `python scripts/load_data.py --db-url postgresql://... --file data/evenements_1500.csv`
5. Lancer l’API Data : `uvicorn app.api:app --reload --port 8000`
6. Lancer l’app Streamlit : `streamlit run app/app.py`

## Commandes utiles
- Exécuter notebooks : `jupyter lab`
- Entraîner modèle : `python train.py --config configs/train.yaml`
- Tests : `pytest tests/`

## Livrables attendus
- E1: API Data + rapport 2–5 pages
- E2/E3: POC IA, API IA, prototype, monitoring
- E4/E5: Application complète, CI/CD, monitoring, résolution d’incidents

Linter Python (flake8/ruff)

Tests unitaires (pytest)

Build image Docker

Entraînement / évaluation automatisés (optionnel selon coût)

Packaging modèle (joblib/onnx)

Déploiement staging (docker-compose / k8s)

Déclencheurs : push sur main, PR merges, tags v*
