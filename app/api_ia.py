from fastapi import FastAPI
import joblib
import pandas as pd

model = joblib.load("models/model.joblib")

app = FastAPI(title="API IA - DevIA")

@app.post("/predict")
def predict(payload: dict):
    df = pd.DataFrame([payload])
    y_pred = model.predict(df)[0]
    return {"prediction": str(y_pred)}
