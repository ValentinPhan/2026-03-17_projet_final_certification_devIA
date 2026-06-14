from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db, init_db
from app.models import Event, EventSchema

app = FastAPI(
    title="API Data",
    description="Mise à disposition des événements ferroviaires",
    version="1.0.0"
)

init_db()


@app.get("/events", response_model=list[EventSchema])
def list_events(limit: int = 5, db: Session = Depends(get_db)):
    return db.query(Event).limit(limit).all()


@app.get("/events/{event_id}", response_model=EventSchema)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id_evenement == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
