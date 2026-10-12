# Journal des modifications

## 2026-10-12 — Sécurité de la configuration

### Modifié
- `.env` retiré du dépôt et ajouté au `.gitignore` (il contenait `API_SECRET_KEY`).
  Le fichier local est conservé ; chaque poste crée le sien avec `cp .env.example .env`.
- `.env.example` complété (toutes les variables, `API_SECRET_KEY=change_me`, `API_IA_URL` pour Docker).
- README : section configuration mise à jour.

## 2026-10-05 — Corrections de bogues

### Corrigé
- **`requirements.txt`** : la dernière ligne était tronquée (`pytest==8.2.`), ce qui faisait échouer
  `pip install` (CI et images Docker). Version corrigée en `pytest==8.2.0` et ajout de `httpx`
  (requis par `fastapi.testclient`).
- **Modèle / API IA — `departement`** : le modèle était entraîné avec `departement` en entier alors que
  l'API et Streamlit l'envoient en texte (`"69"`). La catégorie était donc ignorée silencieusement par le
  `OneHotEncoder`. `train.py` lit désormais `departement` en texte, `models/model.joblib` a été
  réentraîné (scikit-learn 1.3.2) et l'API normalise `69` / `"69"`.
- **`POST /predict`** : entrée validée par un schéma Pydantic (`EventFeatures`). Un payload invalide
  renvoie `422` et une erreur de prédiction `500`, au lieu d'un `200` contenant `{"error": ...}`.
  La réponse inclut maintenant `proba` (confiance du modèle), déjà attendue par Streamlit.
- **`POST /data/filter`** : `{"colonne": "departement", "valeur": "69"}` renvoyait une liste vide
  (comparaison texte / entier). La comparaison se fait désormais en texte.
- **API Data** : `CSV_PATH` et `MODEL_PATH` ont une valeur par défaut — les API démarrent sans `.env`.
  Le CSV est lu une seule fois (cache) au lieu d'être relu à chaque requête.
- **`GET /events`** : `limit` négatif (qui renvoyait toute la table avec SQLite) est refusé (`422`).
- **Streamlit** : les listes `type_evenement` / `exploitant` proposaient des valeurs inconnues du modèle
  (`défaillance`, `autre`, `Autre`) et omettaient `SNCF Voyageurs`, `deraillement`, etc. Ajout d'un
  timeout sur l'appel API et d'un contrôle du département vide.

### Ajouté
- `tests/test_regressions.py` : 10 tests de non-régression.
- `pytest.ini` : `testpaths` et `pythonpath` (les tests se lancent sans `PYTHONPATH`).
- `.gitignore` et suppression des fichiers `__pycache__` versionnés.
