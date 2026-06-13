from fastapi import FastAPI
import joblib
import os

MODEL_PATH = os.getenv("MODEL_PATH")
model = joblib.load(MODEL_PATH)

app = FastAPI(...)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(features: dict):
    ...
