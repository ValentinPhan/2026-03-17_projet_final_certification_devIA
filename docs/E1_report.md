📘 E1 — Rapport Collecte, Stockage & Mise à Disposition
docs/E1_report.md

Résumé  
Ce rapport décrit la collecte, l’ingestion, le stockage et la mise à disposition des données ferroviaires issues du fichier evenements_1500.csv.
L’objectif est de fournir une API Data REST conforme au bloc 1 du référentiel DevIA.

1. Contexte
Données issues d’événements ferroviaires (SNCF, RATP, EPSF).

Format CSV, 1500 lignes.

Objectif : ingestion → stockage → API REST.

2. Description des données
Colonnes :
id_evenement, date, annee, type_evenement, gravite, departement, exploitant, nb_morts, nb_blesses, cause_presumee, contexte, source.

3. Ingestion
Script utilisé : scripts/load_data.py

Validation colonnes

Typage

Création table SQL

Import

4. Stockage
Base SQLite (dev)

PostgreSQL (prod possible)

Table evenements

5. Mise à disposition
API FastAPI (app/api.py)
Endpoints :

GET /events

GET /events/{id}

GET /events/search

POST /events

DELETE /events/{id}

6. RGPD
Pas de données personnelles

Données publiques

Registre RGPD fourni dans docs/RGPD.md