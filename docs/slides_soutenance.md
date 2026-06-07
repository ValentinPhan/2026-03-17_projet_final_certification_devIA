# 🎤 **Slides Architecture – Soutenance DevIA**  
*(Version optimisée pour un jury technique)*

---

# **Slide 1 — Architecture Globale du Projet**
Architecture en 3 services indépendants, orchestrés via Docker :

```
                 Données CSV
                      │
                      ▼
                API Data (FastAPI)
                      │
                      ▼
                Modèle IA (Sklearn)
                      │
                      ▼
                API IA (FastAPI)
                      │
                      ▼
                App Streamlit (UI)
```





---

# **Slide 2 — Architecture Logique**
**Bloc 1 — API Data**  
- Expose les données ferroviaires  
- Endpoints : `/data/raw`, `/data/stats`, `/data/filter`  
- Source unique de vérité  

**Bloc 2 — Modèle IA + API IA**  
- Pipeline sklearn (OHE + RandomForest)  
- Endpoint `/predict`  
- Chargement lazy du modèle  

**Bloc 3 — Application Streamlit**  
- Formulaire utilisateur  
- Appels API IA  
- Visualisation  

---

# **Slide 3 — Architecture Technique (Microservices Docker)**
```
docker-compose.yml
│
├── api_data     → FastAPI (port 8001)
├── api_ia       → FastAPI (port 8000)
└── streamlit    → Frontend (port 8501)
```

Caractéristiques :  
- Services isolés  
- Communication interne via réseau Docker  
- Redémarrage automatique  
- Déploiement simplifié  





---

# **Slide 4 — Architecture API Data**
**Objectif :** exposer les données nettoyées et typées.

Fonctionnalités :  
- Chargement CSV  
- Statistiques descriptives  
- Filtrage dynamique  
- Documentation OpenAPI  

Technos :  
- FastAPI  
- Pandas  
- Pydantic  





---

# **Slide 5 — Architecture Modèle IA**
Pipeline ML :  
- OneHotEncoder  
- RandomForestClassifier  
- Sérialisation joblib  

Avantages :  
- Robuste  
- Interprétable  
- Performant sur petits datasets  
- Compatible production  





---

# **Slide 6 — Architecture API IA**
**Rôle :** encapsuler le modèle IA dans un microservice.

Endpoints :  
- `/health`  
- `/predict`  

Fonctionnement :  
- Validation Pydantic  
- Conversion DataFrame  
- Prédiction via pipeline sklearn  
- Retour JSON  





---

# **Slide 7 — Architecture Streamlit**
**Rôle :** interface utilisateur finale.

Fonctionnalités :  
- Formulaire de saisie  
- Appels API IA  
- Affichage de la prédiction  
- Visualisations  

Connexion API :  
- `API_IA_URL`  
- `API_DATA_URL`  





---

# **Slide 8 — Architecture DevOps (CI/CD)**
Workflows GitHub Actions :  
- `tests.yml` → pytest  
- `build_api.yml` → build Docker API  
- `build_streamlit.yml` → build Docker Streamlit  

Objectifs :  
- Qualité  
- Reproductibilité  
- Déploiement automatisé  





---

# **Slide 9 — Architecture Sécurité & Qualité**
- Validation stricte des entrées (Pydantic)  
- Pas de données personnelles  
- Modèle chargé en lecture seule  
- Microservices isolés  
- Tests unitaires + API + intégration  

---

# **Slide 10 — Conclusion Architecture**
- Architecture **modulaire**, **scalable**, **professionnelle**  
- Séparation claire : Data / IA / UI  
- Microservices Docker  
- CI/CD opérationnel  
- Aligné avec le référentiel DevIA  