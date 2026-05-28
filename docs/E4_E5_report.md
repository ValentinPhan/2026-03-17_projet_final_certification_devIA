🧩 E4/E5 — Rapport Prototype, CI/CD, Monitoring, Résolution d’incidents
docs/E4_E5_report.md

1. Spécifications fonctionnelles
Consultation événements

Recherche filtrée

Prédiction gravité

Interface Streamlit

2. Architecture
Voir docs/architecture.md

3. CI/CD
Pipeline GitHub Actions :

Lint

Tests

Build

(optionnel) Déploiement Docker

4. Monitoring
Logs API

Métriques Prometheus (optionnel)

Dashboard Grafana (optionnel)

5. Résolution d’incidents
Exemple fourni :

API renvoie 500

Analyse logs

Correction SQL

Déploiement patch

1. Introduction
Ce rapport couvre les épreuves E4 et E5 du référentiel DevIA :

E4 : Conception, développement et livraison continue d’une application intégrant un service IA

E5 : Monitoring applicatif et résolution d’incidents

Il s’appuie sur les livrables précédents (E1, E2/E3) et finalise l’ensemble du projet.

2. Analyse du besoin & périmètre fonctionnel
2.1. Contexte
L’application vise à :

Consulter les événements ferroviaires

Filtrer et rechercher

Prédire la gravité d’un événement via un modèle IA

Visualiser les résultats

Fournir une interface simple (Streamlit)

Exposer des API Data et IA

Assurer un monitoring complet

Gérer les incidents et correctifs

2.2. Public cible
Analystes sécurité ferroviaire

Agents d’exploitation

Formateurs / auditeurs

Développeurs internes

2.3. Contraintes
Accessibilité (WCAG)

Sécurité (OWASP API Top 10)

RGPD

Reproductibilité

Éco‑conception

3. Spécifications fonctionnelles
3.1. Fonctionnalités principales
Consultation liste d’événements

Recherche filtrée

Visualisation statistique

Prédiction IA

Ajout / suppression d’événements

Interface Streamlit

API Data + API IA

Monitoring modèle + monitoring applicatif

3.2. User Stories
(Extrait — version complète dans docs/user_stories.md)

US01 : Consulter les événements

US02 : Filtrer par gravité / exploitant

US03 : Prédire la gravité

US04 : Ajouter un événement

US05 : Supprimer un événement

US06 : Dashboard Streamlit

US07 : CI/CD

US08 : Monitoring

4. Architecture technique
4.1. Vue d’ensemble

[Streamlit UI]
       |
       v
[API IA] -----> [Modèle .joblib]
       |
       v
[API Data] ---> [Base SQL]
       |
       v
[Monitoring] -> [Prometheus / Grafana]

4.2. Technologies
Python

FastAPI

Streamlit

scikit‑learn

SQLAlchemy

SQLite / PostgreSQL

GitHub Actions

Docker

Prometheus / Grafana

5. Développement de l’application IA
5.1. Frontend Streamlit
Fonctionnalités :

Formulaire de saisie

Appel API IA

Affichage prédiction

Graphiques (matplotlib / plotly)

Tableaux filtrables

5.2. Backend FastAPI
Deux API :

API Data (app/api.py)

API IA (app/api_ia.py)

5.3. Sécurité
Validation Pydantic

Gestion erreurs

Préparation JWT

Protection contre injections SQL

Logs structurés

6. CI/CD applicatif
6.1. Objectifs
Automatiser tests, build, packaging

Déployer automatiquement

Versionner modèle et données

6.2. Pipeline GitHub Actions
Étapes :

Checkout

Installation dépendances

Tests Pytest

Build Docker

Déploiement staging

(Optionnel) Entraînement modèle automatisé

6.3. Éco‑conception
Jobs courts

Cache pip

Docker multi‑stage

Monitoring consommation CPU/RAM

7. Monitoring applicatif & modèle
7.1. Monitoring modèle
Métriques :

Distribution des prédictions

Dérive des features

Latence API IA

Taux d’erreur

7.2. Monitoring applicatif
Logs JSON

Métriques Prometheus

Dashboard Grafana

Alertes (seuils)

7.3. Exemple de métriques
api_latency_seconds

prediction_count_total

prediction_error_total

8. Gestion des incidents (E5)
8.1. Objectif
Démontrer la capacité à :

Diagnostiquer

Reproduire

Corriger

Documenter

8.2. Incident simulé
Symptôme : l’API Data renvoie 500 sur /events/search.

Diagnostic
Analyse logs → erreur SQL

Reproduction locale

Correction : paramètre manquant dans la requête

Correctif
Patch SQL

Ajout tests

Déploiement via CI/CD

Documentation
Fiche incident dans docs/incidents/incident_01.md

9. Accessibilité & éco‑conception
9.1. Accessibilité
Contrastes respectés

Labels explicites

Navigation clavier

Compatibilité lecteurs d’écran

9.2. Éco‑conception
Modèle léger

Pas de GPU

API stateless

Cache local

Docker optimisé

10. Conclusion
Les objectifs E4/E5 sont atteints :

✔ Application IA complète

✔ API Data + API IA

✔ Interface Streamlit

✔ CI/CD opérationnel

✔ Monitoring modèle + applicatif

✔ Gestion d’incidents

✔ Documentation complète

✔ Conformité RGPD, sécurité, accessibilité