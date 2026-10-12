from pathlib import Path
from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = os.getenv("MODEL_PATH") or str(BASE_DIR / "models" / "model.joblib")

# Colonnes attendues par le pipeline (cf. train.py)
FEATURES = ["type_evenement", "departement", "exploitant", "nb_morts", "nb_blesses"]

app = FastAPI(
    title="API IA",
    description="Prediction de la gravite d'un evenement",
    version="1.0.0",
)

model = joblib.load(MODEL_PATH)

# --- Monitoring Prometheus ---
# Expose les metriques (latence, nb de requetes, codes HTTP...) sur /metrics
try:
    from prometheus_fastapi_instrumentator import Instrumentator

    Instrumentator().instrument(app).expose(app, endpoint="/metrics")
except Exception:  # pragma: no cover - le monitoring est optionnel
    pass


class EventFeatures(BaseModel):
    type_evenement: str
    # Accepte "69" ou 69 : normalise en texte comme a l'entrainement
    departement: Union[str, int]
    exploitant: str
    nb_morts: int = Field(ge=0)
    nb_blesses: int = Field(ge=0)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: EventFeatures):
    data = features.model_dump()
    data["departement"] = str(data["departement"]).strip()
    df = pd.DataFrame([data], columns=FEATURES)

    try:
        y_pred = model.predict(df)[0]
        proba = float(model.predict_proba(df)[0].max())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur de prediction : {e}")

    return {"gravite_predite": str(y_pred), "proba": proba}
