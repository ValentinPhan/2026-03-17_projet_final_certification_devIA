from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
CSV_PATH = os.getenv("CSV_EVENTS_PATH")

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # 1) Créer les tables
    Base.metadata.create_all(bind=engine)

    # 2) Charger le CSV dans la table si vide
    with engine.connect() as conn:
        result = conn.execute("SELECT COUNT(*) FROM evenements")
        count = result.fetchone()[0]

        if count == 0:
            df = pd.read_csv(CSV_PATH)
            df.to_sql("evenements", conn, if_exists="append", index=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

