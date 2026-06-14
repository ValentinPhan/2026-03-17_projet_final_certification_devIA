from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db, init_db
from app.models import Event, EventSchema
import pandas as pd
import os

app = FastAPI(
    title="API Data",
    description="Mise à disposition des événements ferroviaires",
    version="1.0.0"
)

init_db()

CSV_PATH = os.getenv("CSV_EVENTS_PATH")


@app.get("/events", response_model=list[EventSchema])
def list_events(limit: int = 5, db: Session = Depends(get_db)):
    return db.query(Event).limit(limit).all()


@app.get("/events/{event_id}", response_model=EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id_evenement == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


# ---------------------------
#   ENDPOINTS ATTENDUS PAR LES TESTS
# ---------------------------

@app.get("/data/raw")
def get_raw_data():
    df = pd.read_csv(CSV_PATH)
    return df.to_dict(orient="records")


@app.get("/data/columns")
def get_columns():
    df = pd.read_csv(CSV_PATH)
    return {"colonnes": df.columns.tolist()}


@app.post("/data/filter")
def filter_data(payload: dict):
    colonne = payload.get("colonne")
    valeur = payload.get("valeur")

    df = pd.read_csv(CSV_PATH)

    if colonne not in df.columns:
        raise HTTPException(status_code=400, detail="Colonne invalide")

    filtered = df[df[colonne] == valeur]
    return filtered.to_dict(orient="records")
