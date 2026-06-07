from fastapi.testclient import TestClient
from app.api_ia import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_predict():
    payload = {
        "type_evenement": "collision",
        "departement": "69",
        "exploitant": "SNCF Réseau",
        "nb_morts": 0,
        "nb_blesses": 2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "gravite_predite" in response.json()
