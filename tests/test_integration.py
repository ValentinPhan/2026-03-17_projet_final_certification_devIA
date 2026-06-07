import joblib
import pandas as pd
from fastapi.testclient import TestClient
from app.api_ia import app

client = TestClient(app)

def test_full_pipeline():
    model = joblib.load("models/model.joblib")

    sample = {
        "type_evenement": "collision",
        "departement": "75",
        "exploitant": "SNCF Réseau",
        "nb_morts": 0,
        "nb_blesses": 1
    }

    # API IA
    response = client.post("/predict", json=sample)
    assert response.status_code == 200

    # Modèle local
    df = pd.DataFrame([sample])
    local_pred = model.predict(df)[0]

    # Cohérence API ↔ modèle
    assert response.json()["gravite_predite"] == str(local_pred)
