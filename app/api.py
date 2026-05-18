from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
import pandas as pd

DB_URL = "sqlite:///data.db"  # à remplacer par PostgreSQL si besoin
engine = create_engine(DB_URL)

app = FastAPI(title="API Data - DevIA")

@app.get("/events")
def list_events(limit: int = 100):
    df = pd.read_sql("SELECT * FROM evenements LIMIT :limit", engine, params={"limit": limit})
    return df.to_dict(orient="records")

@app.get("/events/{event_id}")
def get_event(event_id: int):
    query = "SELECT * FROM evenements WHERE id_evenement = :id"
    df = pd.read_sql(query, engine, params={"id": event_id})
    if df.empty:
        raise HTTPException(404, "Événement introuvable")
    return df.to_dict(orient="records")[0]
