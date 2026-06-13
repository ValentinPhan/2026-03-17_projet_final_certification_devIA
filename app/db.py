from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import pandas as pd
import os

DB_URL = os.getenv("DB_URL")
CSV_PATH = os.getenv("CSV_EVENTS_PATH")

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    # charger CSV si table vide

def get_db():
    ...
