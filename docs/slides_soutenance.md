Slide 1 — Titre & Contexte
Projet : Analyse & Prédiction d’Événements Ferroviaires  
Certification Développeur IA — Simplon 2026  
Auteur : Valentin Phan

Objectifs techniques :

Collecte & ingestion de données

API Data & API IA

Modèle ML reproductible

CI/CD & Monitoring

Application complète intégrant un service IA

Slide 2 — Architecture Globale
Architecture technique :

Frontend : Streamlit

Backend : FastAPI (API Data + API IA)

Modèle IA : scikit‑learn (RandomForest)

Base de données : SQLite / PostgreSQL

CI/CD : GitHub Actions

Monitoring : Prometheus + Grafana

Slide 3 — Pipeline de Données (E1)
Source : evenements_1500.csv

Validation & typage

Import SQL via script Python

MCD / MLD Merise

API Data REST exposée via FastAPI

Documentation OpenAPI

Slide 4 — Modèle IA (E2/E3)
Pipeline ML :

OneHotEncoder

RandomForestClassifier

Split train/test

Sauvegarde .joblib

Résultats :

Accuracy ≈ 0.82

F1‑macro ≈ 0.78

Slide 5 — API IA
Endpoints :

POST /predict

Validation Pydantic

Gestion erreurs

Logs structurés

Latence < 50 ms en local

Payload exemple :

{
  "type_evenement": "collision",
  "departement": "44",
  "exploitant": "SNCF Réseau",
  "nb_morts": 1,
  "nb_blesses": 7
}

Slide 6 — Application Streamlit
Fonctionnalités :

Formulaire de prédiction

Visualisation des événements

Graphiques interactifs

Intégration API Data + API IA

Slide 7 — CI/CD (E4)
Pipeline GitHub Actions :

Lint

Tests Pytest

Build Docker

Déploiement staging

Versionnement modèle & données

Éco‑conception :

Jobs courts

Cache pip

Docker multi‑stage

Slide 8 — Monitoring (E5)
Monitoring modèle :

Dérive des features

Distribution des prédictions

Latence API IA

Taux d’erreur

Monitoring applicatif :

Logs JSON

Métriques Prometheus

Dashboard Grafana

Slide 9 — Incident & Résolution (E5)
Incident simulé :

API Data renvoie 500 sur /events/search

Diagnostic :

Analyse logs → erreur SQL

Reproduction locale

Correction paramètre manquant

Ajout test unitaire

Déploiement via CI/CD

Slide 10 — Résultats & Livrables
Livrables produits :

API Data complète

API IA complète

Modèle ML reproductible

Application Streamlit

CI/CD opérationnel

Monitoring modèle + app

Rapports E1 → E5

Backlog, user stories, MCD/MLD, RGPD

Slide 11 — Conclusion
Projet complet, industrialisable

Architecture claire et modulaire

IA intégrée proprement dans un workflow DevOps

Monitoring et gestion d’incidents maîtrisés

Aligné avec le référentiel DevIA 2026

Slide 12 — Questions
Merci pour votre attention.