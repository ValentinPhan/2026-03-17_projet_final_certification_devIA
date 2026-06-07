from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd
from pathlib import Path

# -----------------------------
# Configuration
# -----------------------------
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "evenements_1500.csv"

app = FastAPI(
    title="API Data – Projet DevIA",
    description="API REST Data conforme au référentiel DevIA (Bloc 1 / E1).",
    version="1.0.0"
)

# CORS (pour Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Chargement des données
# -----------------------------
def load_data():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Fichier introuvable : {DATA_PATH}")
    return pd.read_csv(DATA_PATH)

# -----------------------------
# Modèles Pydantic
# -----------------------------
class FilterRequest(BaseModel):
    colonne: str
    valeur: str

# -----------------------------
# Endpoints
# -----------------------------

@app.get("/data/raw", summary="Renvoie l'intégralité du dataset")
def get_raw_data():
    try:
        df = load_data()
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/data/sample", summary="Renvoie un échantillon du dataset")
def get_sample(n: int = 5):
    try:
        df = load_data()
        return df.sample(n=min(n, len(df))).to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/data/columns", summary="Renvoie la liste des colonnes")
def get_columns():
    try:
        df = load_data()
        return {"colonnes": df.columns.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/data/stats", summary="Statistiques descriptives")
def get_stats():
    try:
        df = load_data()
        return df.describe(include="all").fillna("").to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/data/filter", summary="Filtre les données selon une colonne et une valeur")
def filter_data(req: FilterRequest):
    try:
        df = load_data()
        if req.colonne not in df.columns:
            raise HTTPException(status_code=400, detail="Colonne inconnue.")
        filtered = df[df[req.colonne].astype(str) == req.valeur]
        return filtered.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
