from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy import text
from sqlalchemy.orm import Session
from pathlib import Path
import pandas as pd

from app.db import get_db, init_db
from app.models import Event
from app.models import EventSchema

from dotenv import load_dotenv
import os

load_dotenv()

CSV_PATH = os.getenv("CSV_EVENTS_PATH")
DB_URL = os.getenv("DB_URL")

app = FastAPI(
    title="API Data - DevIA",
    description="API de mise à disposition des événements ferroviaires",
    version="1.1.0"
)

init_db()

# -------------------------------------------------------------------
# ENDPOINT 1 — LISTE AVEC PAGINATION (limit + offset)
# -------------------------------------------------------------------
'''@app.get("/events")
def list_events(
    limit: int = Query(10, ge=1, le=500),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    query = text("""
        SELECT * FROM evenements
        LIMIT :limit OFFSET :offset
    """)

    rows = db.execute(query, {"limit": limit, "offset": offset}).fetchall()

    # total pour pagination
    total = db.execute(text("SELECT COUNT(*) FROM evenements")).scalar()

    return {
        "total": total,
        "count": len(rows),
        "limit": limit,
        "offset": offset,
        "results": [dict(row._mapping) for row in rows]
    }'''

@app.get("/events", response_model=list[EventSchema])
def list_events(limit: int = 5, db: Session = Depends(get_db)):
    return db.query(Event).limit(limit).all()

# -------------------------------------------------------------------
# ENDPOINT 2 — FILTRES (type, gravité, exploitant)
# -------------------------------------------------------------------
@app.get("/events/search", response_model=list[Event])
def search_events(
    type_evenement: str | None = None,
    gravite: str | None = None,
    exploitant: str | None = None,
    db: Session = Depends(get_db)
):
    conditions = []
    params = {}

    if type_evenement:
        conditions.append("type_evenement = :type_evenement")
        params["type_evenement"] = type_evenement

    if gravite:
        conditions.append("gravite = :gravite")
        params["gravite"] = gravite

    if exploitant:
        conditions.append("exploitant = :exploitant")
        params["exploitant"] = exploitant

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    query = text(f"SELECT * FROM evenements WHERE {where_clause}")
    rows = db.execute(query, params).fetchall()

    return [dict(row._mapping) for row in rows]

# -------------------------------------------------------------------
# ENDPOINT 3 — GET PAR ID
# -------------------------------------------------------------------
'''@app.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int, db: Session = Depends(get_db)):
    query = text("SELECT * FROM evenements WHERE id_evenement = :id")
    row = db.execute(query, {"id": event_id}).fetchone()

    if not row:
        raise HTTPException(404, "Événement introuvable")

    return dict(row._mapping)'''
@app.get("/events/{event_id}", response_model=EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id_evenement == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# -------------------------------------------------------------------
# ENDPOINT 4 — AJOUT D’UN ÉVÉNEMENT
# -------------------------------------------------------------------
@app.post("/events", response_model=Event)
def create_event(event: Event, db: Session = Depends(get_db)):
    query = text("""
        INSERT INTO evenements (
            id_evenement, date, annee, type_evenement, gravite,
            departement, exploitant, nb_morts, nb_blesses,
            cause_presumee, contexte, source
        )
        VALUES (
            :id_evenement, :date, :annee, :type_evenement, :gravite,
            :departement, :exploitant, :nb_morts, :nb_blesses,
            :cause_presumee, :contexte, :source
        )
    """)

    db.execute(query, event.dict())
    db.commit()

    return event

# -------------------------------------------------------------------
# ENDPOINT 5 — SUPPRESSION
# -------------------------------------------------------------------
@app.delete("/events/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    query = text("DELETE FROM evenements WHERE id_evenement = :id")
    result = db.execute(query, {"id": event_id})
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(404, "Événement introuvable")

    return {"status": "deleted", "id": event_id}
