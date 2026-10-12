from functools import lru_cache

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db import CSV_PATH, get_db, init_db
from app.models import Event, EventSchema
import pandas as pd

app = FastAPI(
    title="API Data",
    description="Mise a disposition des evenements ferroviaires",
    version="1.0.0",
)

init_db()

# --- Monitoring Prometheus ---
# Expose les metriques (latence, nb de requetes, codes HTTP...) sur /metrics
try:
    from prometheus_fastapi_instrumentator import Instrumentator

    Instrumentator().instrument(app).expose(app, endpoint="/metrics")
except Exception:  # pragma: no cover - le monitoring est optionnel
    pass



@lru_cache(maxsize=1)
def load_csv() -> pd.DataFrame:
    """Lit le CSV une seule fois (departement en texte, ex : "69", "2A")."""
    return pd.read_csv(CSV_PATH, dtype={"departement": str})


@app.get("/events", response_model=list[EventSchema])
def list_events(limit: int = Query(5, ge=1), db: Session = Depends(get_db)):
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
    df = load_csv()
    return df.to_dict(orient="records")


@app.get("/data/columns")
def get_columns():
    df = load_csv()
    return {"colonnes": df.columns.tolist()}


@app.post("/data/filter")
def filter_data(payload: dict):
    colonne = payload.get("colonne")
    valeur = payload.get("valeur")

    df = load_csv()

    if colonne not in df.columns:
        raise HTTPException(status_code=400, detail="Colonne invalide")

    # Comparaison en texte : "69" et 69 doivent donner le meme resultat
    filtered = df[df[colonne].astype(str) == str(valeur)]
    return filtered.to_dict(orient="records")
