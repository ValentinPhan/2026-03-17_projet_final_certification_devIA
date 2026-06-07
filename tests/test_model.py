import joblib
import pandas as pd
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "model.joblib"

def test_model_file_exists():
    assert MODEL_PATH.exists(), "Le fichier model.joblib est introuvable."

def test_model_prediction_shape():
    model = joblib.load(MODEL_PATH)

    sample = pd.DataFrame([{
        "type_evenement": "collision",
        "departement": "69",
        "exploitant": "SNCF Réseau",
        "nb_morts": 0,
        "nb_blesses": 3
    }])

    pred = model.predict(sample)
    assert len(pred) == 1, "La prédiction doit contenir 1 élément."
