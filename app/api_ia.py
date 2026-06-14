from fastapi import FastAPI
import joblib
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")

app = FastAPI(
    title="API IA",
    description="Prédiction de la gravité d'un événement",
    version="1.0.0"
)

model = joblib.load(MODEL_PATH)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: dict):
    try:
        # Convertir en DataFrame avec colonnes
        df = pd.DataFrame([features])

        # Prédiction
        y_pred = model.predict(df)[0]

        return {"gravite_predite": str(y_pred)}

    except Exception as e:
        return {"error": str(e)}
