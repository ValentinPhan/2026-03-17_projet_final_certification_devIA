🧠 Projet Final – Certification Développeur IA
Analyse d’événements ferroviaires & Prédiction de gravité
Ce projet a été réalisé dans le cadre de la Certification Développeur IA – Simplon 2026.
Il combine Data Engineering, Machine Learning, APIs FastAPI, CI/CD GitHub Actions, et interface utilisateur Streamlit.

L’objectif :
➡️ Analyser des événements ferroviaires  
➡️ Prédire automatiquement la gravité d’un événement  
➡️ Exposer les données et les prédictions via des APIs  
➡️ Fournir une interface simple pour les utilisateurs

📦 Architecture du projet
Code
2026-03-17_projet_final_certification_devIA/
│
├── app/
│   ├── api.py               → API Data (FastAPI)
│   ├── api_ia.py            → API IA (FastAPI)
│   ├── db.py                → Connexion + initialisation BDD
│   ├── models.py            → Modèles SQLAlchemy + Pydantic
│   └── __init__.py
│
├── data/
│   ├── evenements_1500.csv  → Données source
│   └── events.db            → Base SQLite générée automatiquement
│
├── models/
│   └── model.joblib         → Modèle ML entraîné
│
├── tests/
│   ├── test_api.py
│   ├── test_api_data.py
│   ├── test_api_ia.py
│   └── test_integration.py
│
├── .github/workflows/
│   └── ci.yml               → Pipeline CI GitHub Actions
│
├── conftest.py              → Chargement automatique du .env pour Pytest
├── pytest.ini
├── .env
├── .env.example
├── requirements.txt
└── README.md
⚙️ Installation & Configuration
1. Cloner le projet
bash
git clone https://github.com/ValentinPhan/2026-03-17_projet_final_certification_devIA.git
cd 2026-03-17_projet_final_certification_devIA
2. Créer l’environnement Python
bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
3. Configurer les variables d’environnement
Créer un fichier .env :

bash
cp .env.example .env
Contenu :

env
API_DATA_PORT=8001
API_IA_PORT=8000
STREAMLIT_PORT=8501

DB_URL=sqlite:///./data/events.db
CSV_EVENTS_PATH=./data/evenements_1500.csv
MODEL_PATH=./models/model.joblib
🚀 Lancement des services
API Data
bash
uvicorn app.api:app --reload --port $API_DATA_PORT
API IA
bash
uvicorn app.api_ia:app --reload --port $API_IA_PORT
Interface Streamlit
bash
streamlit run app/app.py
🧬 Modèle Machine Learning
Le modèle est entraîné via :

bash
python scripts/train_model.py
Il utilise :

preprocessing scikit-learn

modèle supervisé

sauvegarde via joblib

Le modèle final est stocké dans :

Code
models/model.joblib
🗄️ Base de données
La base SQLite est générée automatiquement au lancement de l’API Data :

création de la table evenements

chargement automatique du CSV si la table est vide

Aucun script manuel n’est nécessaire.

🧪 Tests automatisés (CI)
Les tests sont exécutés via :

bash
pytest -q
La CI GitHub Actions :

installe les dépendances

initialise la base

exécute tous les tests

valide la conformité du projet

Fichier : .github/workflows/ci.yml

🐳 Docker (optionnel)
Un docker-compose.yml est fourni pour lancer :

API Data

API IA

Streamlit

Avec :

bash
docker compose up --build
📚 Documentation API
FastAPI génère automatiquement la documentation :

API Data :
👉 http://localhost:8001/docs

API IA :
👉 http://localhost:8000/docs

🎤 Soutenance
Ce projet couvre :

Collecte & préparation des données

Modélisation ML

APIs REST

CI/CD

Docker

Interface utilisateur

Documentation technique

Il répond aux compétences du référentiel DevIA (C1 → C21).

🏁 Conclusion
Ce projet propose une architecture complète, modulaire et professionnelle :

APIs FastAPI

Base SQLite auto-initialisée

Modèle ML prédictif

Interface utilisateur

CI GitHub Actions

Documentation claire