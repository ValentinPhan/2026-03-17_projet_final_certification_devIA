from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_get_raw_data():
    response = client.get("/data/raw")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_columns():
    response = client.get("/data/columns")
    assert response.status_code == 200
    assert "colonnes" in response.json()

def test_filter_data():
    payload = {"colonne": "departement", "valeur": "69"}
    response = client.post("/data/filter", json=payload)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
