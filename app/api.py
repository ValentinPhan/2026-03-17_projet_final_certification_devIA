from fastapi import FastAPI, Depends
from app.db import init_db, get_db
from app.models import Event

app = FastAPI(...)
init_db()

@app.get("/events")
def list_events(...):
    ...

@app.get("/events/{event_id}")
def get_event(...):
    ...
