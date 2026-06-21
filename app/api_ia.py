from fastapi import FastAPI
import joblib
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_PATH = os.getenv("MODEL_PATH")

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


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(features: dict):
    try:
        # Convertir en DataFrame avec colonnes
        df = pd.DataFrame([features])

        # Prediction
        y_pred = model.predict(df)[0]

        return {"gravite_predite": str(y_pred)}

    except Exception as e:
        return {"error": str(e)}
