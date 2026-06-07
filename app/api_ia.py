from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Literal, Optional
from pathlib import Path
import joblib
import pandas as pd

# -----------------------------
# Config
# -----------------------------
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "model.joblib"

app = FastAPI(
    title="API IA – Projet DevIA",
    description="API de prédiction de la gravité d'un événement ferroviaire.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Chargement du modèle
# -----------------------------
model = None

def load_model():
    global model
    if model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(f"Modèle introuvable : {MODEL_PATH}")
        model = joblib.load(MODEL_PATH)
    return model

# -----------------------------
# Schémas d'entrée / sortie
# -----------------------------
class EventFeatures(BaseModel):
    type_evenement: str = Field(..., description="Type d'événement")
    departement: str = Field(..., description="Code département")
    exploitant: str = Field(..., description="Exploitant (SNCF Réseau, RATP, etc.)")
    nb_morts: int = Field(..., ge=0, description="Nombre de morts")
    nb_blesses: int = Field(..., ge=0, description="Nombre de blessés")
    # Ajoute ici d'autres features si ton modèle en utilise


class PredictionResponse(BaseModel):
    gravite_predite: str
    proba: Optional[float] = None


# -----------------------------
# Endpoints
# -----------------------------
@app.get("/health", summary="Vérifie l'état de l'API IA")
def health_check():
    try:
        load_model()
        return {"status": "ok", "model_loaded": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict", response_model=PredictionResponse, summary="Prédit la gravité d'un événement")
def predict(event: EventFeatures):
    try:
        clf = load_model()

        # Conversion en DataFrame pour respecter le pipeline sklearn
        df = pd.DataFrame([event.dict()])

        y_pred = clf.predict(df)[0]

        proba = None
        if hasattr(clf, "predict_proba"):
            proba = float(max(clf.predict_proba(df)[0]))

        return PredictionResponse(
            gravite_predite=str(y_pred),
            proba=proba,
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
