"""Tests de non-regression des bogues corriges (filtre, /predict, /events)."""
from fastapi.testclient import TestClient

from app.api import app as app_data
from app.api_ia import app as app_ia, model

client_data = TestClient(app_data)
client_ia = TestClient(app_ia)

SAMPLE = {
    "type_evenement": "collision",
    "departement": "69",
    "exploitant": "SNCF Réseau",
    "nb_morts": 0,
    "nb_blesses": 2,
}


# --- API Data ---

def test_filter_departement_str_et_int_identiques():
    r_str = client_data.post("/data/filter", json={"colonne": "departement", "valeur": "69"})
    r_int = client_data.post("/data/filter", json={"colonne": "departement", "valeur": 69})
    assert r_str.status_code == r_int.status_code == 200
    assert len(r_str.json()) > 0
    assert r_str.json() == r_int.json()


def test_filter_colonne_invalide():
    r = client_data.post("/data/filter", json={"colonne": "inconnue", "valeur": "x"})
    assert r.status_code == 400


def test_events_limit_respectee():
    r = client_data.get("/events?limit=3")
    assert r.status_code == 200
    assert len(r.json()) == 3


def test_events_limit_negative_refusee():
    r = client_data.get("/events?limit=-1")
    assert r.status_code == 422


def test_get_event_existant():
    r = client_data.get("/events/1")
    assert r.status_code == 200
    assert r.json()["id_evenement"] == 1


# --- API IA ---

def test_modele_entraine_avec_departement_texte():
    categories = model.named_steps["preprocess"].named_transformers_["cat"].categories_
    assert "69" in list(categories[1])


def test_predict_retourne_classe_et_proba():
    r = client_ia.post("/predict", json=SAMPLE)
    assert r.status_code == 200
    body = r.json()
    assert body["gravite_predite"] in {str(c) for c in model.classes_}
    assert 0.0 <= body["proba"] <= 1.0


def test_predict_departement_int_equivaut_a_str():
    r_str = client_ia.post("/predict", json=SAMPLE)
    r_int = client_ia.post("/predict", json={**SAMPLE, "departement": 69})
    assert r_str.json() == r_int.json()


def test_predict_payload_incomplet_renvoie_422():
    r = client_ia.post("/predict", json={"type_evenement": "collision"})
    assert r.status_code == 422


def test_predict_valeurs_negatives_refusees():
    r = client_ia.post("/predict", json={**SAMPLE, "nb_morts": -1})
    assert r.status_code == 422
