# 📘 **DOCUMENTATION TECHNIQUE – Projet Final DevIA**

## 1. Présentation générale

Ce document décrit l’architecture technique du projet final du parcours **Développeur en Intelligence Artificielle – Simplon 2026**.  
Le système complet repose sur trois composants principaux :

- **API Data** (FastAPI)  
- **API IA** (FastAPI + modèle ML)  
- **Application Streamlit** (Frontend utilisateur)  

L’ensemble est orchestré via **Docker Compose**, testé via **pytest**, et automatisé via **GitHub Actions**.

---

# 2. Architecture globale

## 2.1 Vue d’ensemble

```
                 ┌──────────────────┐
                 │   Données CSV    │
                 │ evenements_1500  │
                 └────────┬─────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     API Data       │
                │   (FastAPI)        │
                └────────┬───────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   Modèle IA        │
                │ RandomForest + OHE │
                └────────┬───────────┘
                          │
                          ▼
                ┌────────────────────┐
                │     API IA         │
                │   (FastAPI)        │
                └────────┬───────────┘
                          │
                          ▼
                ┌────────────────────┐
                │   Streamlit App    │
                │  (Frontend IA)     │
                └────────────────────┘
```

---

# 3. API Data (FastAPI)

## 3.1 Objectif
Exposer les données ferroviaires sous forme d’API REST :

- accès brut  
- statistiques  
- filtrage  
- métadonnées  

## 3.2 Endpoints

| Méthode | Route          | Description |
|--------|----------------|-------------|
| GET    | `/data/raw`    | Renvoie l’intégralité du dataset |
| GET    | `/data/sample` | Renvoie un échantillon |
| GET    | `/data/stats`  | Statistiques descriptives |
| GET    | `/data/columns`| Liste des colonnes |
| POST   | `/data/filter` | Filtrage dynamique |

## 3.3 Technologies

- FastAPI  
- Pydantic  
- Pandas  
- Uvicorn  

---

# 4. Modèle IA

## 4.1 Objectif
Prédire la **gravité** d’un événement ferroviaire.

## 4.2 Pipeline ML

- **OneHotEncoder** pour les variables catégorielles  
- **RandomForestClassifier** pour la prédiction  
- Sérialisation via **joblib**  

## 4.3 Script d’entraînement

Le fichier `train.py` :

- charge les données  
- split train/test  
- construit le pipeline  
- entraîne le modèle  
- génère un rapport de classification  
- sauvegarde `models/model.joblib`  

## 4.4 Choix du modèle

RandomForest a été choisi pour :

- sa robustesse  
- sa capacité à gérer les variables mixtes  
- sa bonne performance sur petits datasets  
- sa faible sensibilité au scaling  

---

# 5. API IA (FastAPI)

## 5.1 Objectif
Exposer le modèle IA via une API REST.

## 5.2 Endpoints

| Méthode | Route      | Description |
|--------|------------|-------------|
| GET    | `/health`  | Vérifie l’état du modèle |
| POST   | `/predict` | Renvoie la gravité prédite |

## 5.3 Fonctionnement

1. Chargement lazy du modèle joblib  
2. Validation des entrées via Pydantic  
3. Conversion en DataFrame  
4. Prédiction via pipeline sklearn  
5. Retour JSON  

---

# 6. Application Streamlit

## 6.1 Objectif
Interface utilisateur permettant :

- la saisie des caractéristiques d’un événement  
- l’appel à l’API IA  
- l’affichage de la prédiction  
- la visualisation des données  

## 6.2 Fonctionnement

- Formulaire utilisateur  
- Requête HTTP vers `/predict`  
- Affichage du résultat  
- Gestion des erreurs API  

---

# 7. Conteneurisation (Docker)

## 7.1 Dockerfile API IA
- Python 3.10 slim  
- Installation requirements  
- Copie du code + modèle  
- Lancement Uvicorn  

## 7.2 Dockerfile Streamlit
- Python 3.10 slim  
- Installation requirements  
- Copie du code  
- Lancement Streamlit  

## 7.3 docker-compose.yml

Services :

- `api_data` → FastAPI (port 8001)  
- `api` → FastAPI IA (port 8000)  
- `streamlit` → Frontend (port 8501)  

Communication interne via réseau Docker.

---

# 8. Tests automatisés

## 8.1 Types de tests

| Type | Fichier | Objectif |
|------|---------|----------|
| Test modèle | `test_model.py` | Vérifier la prédiction |
| Test API Data | `test_api_data.py` | Vérifier les endpoints |
| Test API IA | `test_api_ia.py` | Vérifier `/predict` |
| Test intégration | `test_integration.py` | Cohérence API ↔ modèle |

## 8.2 Commande

```
pytest -v
```

---

# 9. CI/CD (GitHub Actions)

## 9.1 Workflows

- `tests.yml` → exécution des tests  
- `build_api.yml` → build Docker API  
- `build_streamlit.yml` → build Docker Streamlit  

## 9.2 Objectifs

- garantir la qualité  
- automatiser les builds  
- préparer le déploiement  

---

# 10. Sécurité & bonnes pratiques

- Validation stricte des entrées (Pydantic)  
- Pas de chargement dynamique non contrôlé  
- Pas de données personnelles  
- API isolées dans des conteneurs  
- Modèle chargé en lecture seule  

---

# 11. Déploiement

## 11.1 Local

```
docker compose up --build
```

## 11.2 Cloud (options)

- Render  
- Railway  
- Azure App Service  
- Streamlit Cloud  

---

# 12. Conclusion

Cette architecture respecte :

- les **3 blocs** du référentiel DevIA  
- les bonnes pratiques IA  
- les bonnes pratiques API  
- les bonnes pratiques DevOps  
- les attentes du jury  

Elle est modulaire, scalable, testée, documentée et prête pour la production.
