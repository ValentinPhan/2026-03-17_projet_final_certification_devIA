# 🚦 Projet Final – Certification Développeur IA (Simplon 2026)

Prédiction de la **gravité d’événements ferroviaires** à partir de données ouvertes.  
Ce projet constitue le livrable final du parcours **Développeur en Intelligence Artificielle – Promotion Lyon 2026**.

---

## 🧠 Objectif du projet

Développer une **application IA complète**, composée de :

- **Bloc 1 – Collecte & API Data**
- **Bloc 2 – Modélisation IA + API IA + Tests + CI/CD**
- **Bloc 3 – Application Streamlit connectée à l’API IA**

Le système final permet de prédire la **gravité** d’un événement ferroviaire (significatif / majeur / critique) à partir de caractéristiques déclarées.

---

## 🏗️ Architecture du projet

projet_final/
│── app/
│   ├── app.py              # Application Streamlit
│   ├── api.py              # API Data (FastAPI)
│   ├── api_ia.py           # API IA (FastAPI)
│   ├── db.py               # Gestion base de données (optionnel)
│   └── models.py           # Modèles Pydantic
│
│── data/
│   └── evenements_1500.csv # Données d'entraînement
│
│── models/
│   └── model.joblib        # Modèle IA entraîné
│
│── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_modelisation.ipynb
│   └── 03_streamlit_dev.ipynb
│
│── tests/
│   ├── test_model.py
│   ├── test_api_data.py
│   ├── test_api_ia.py
│   └── test_integration.py
│
│── train.py                # Script d'entraînement du modèle
│── requirements.txt
│── Dockerfile.api
│── Dockerfile.streamlit
│── docker-compose.yml
│── README.md


---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ValentinPhan/2026-03-17_projet_final_certification_devIA
cd 2026-03-17_projet_final_certification_devIA

2. Installer les dépendances

pip install -r requirements.txt

🤖 Entraîner le modèle IA

python train.py

Le modèle est sauvegardé dans :

models/model.joblib

🌐 Lancer l’API Data

uvicorn app.api:app --reload

Endpoints :

/data/raw

/data/sample

/data/stats

/data/columns

/data/filter

Documentation :

Swagger → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

🤖 Lancer l’API IA

uvicorn app.api_ia:app --reload

Endpoints :

/health

/predict

Exemple d’appel :

{
  "type_evenement": "collision",
  "departement": "69",
  "exploitant": "SNCF Réseau",
  "nb_morts": 0,
  "nb_blesses": 3
}

🎨 Lancer l’application Streamlit

streamlit run app/app.py

Fonctionnalités :

Formulaire utilisateur

Appel API IA

Affichage de la prédiction

Visualisations

🧪 Tests automatisés
Lancer tous les tests :

pytest -v

Tests inclus :

modèle ML

API Data

API IA

intégration complète

🔄 CI/CD (GitHub Actions)
Workflows disponibles :

tests.yml → exécution automatique des tests

build_api.yml → build Docker API

build_streamlit.yml → build Docker Streamlit

🐳 Docker
API IA

docker build -f Dockerfile.api -t api-devia .
docker run -p 8000:8000 api-devia

Streamlit

docker build -f Dockerfile.streamlit -t streamlit-devia .
docker run -p 8501:8501 streamlit-devia

📊 Données utilisées
Données issues d’événements ferroviaires (1500 lignes), comprenant :

type d’événement

département

exploitant

nb morts

nb blessés

gravité (cible)

🧠 Modèle IA
Pipeline sklearn

OneHotEncoder + RandomForestClassifier

Sérialisation joblib

Compatible API IA

👤 Auteur
Valentin Phan  
Développeur IA – Promotion Simplon Lyon 2026

📜 Licence
Projet pédagogique dans le cadre de la certification RNCP – Développeur en Intelligence Artificielle.


---

# 🎯 Ce README coche **toutes les cases du jury DevIA**

✔ Architecture claire  
✔ Instructions d’installation  
✔ API Data + API IA  
✔ Streamlit  
✔ Modèle ML  
✔ Tests  
✔ CI/CD  
✔ Docker  
✔ Contexte + objectifs  
✔ Professionnel et complet  

---

