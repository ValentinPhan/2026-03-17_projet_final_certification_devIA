import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from app.models import Base

load_dotenv()

# URL de la base (par defaut : SQLite dans le dossier data/)
DB_URL = os.getenv("DB_URL", "sqlite:///./data/events.db")
CSV_PATH = os.getenv("CSV_EVENTS_PATH", "./data/evenements_1500.csv")

# check_same_thread n'est utile que pour SQLite
connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}

engine = create_engine(DB_URL, connect_args=connect_args)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db():
    """Cree les tables et charge le CSV dans la base si elle est vide."""
    if DB_URL.startswith("sqlite:///"):
        db_file = DB_URL.replace("sqlite:///", "", 1)
        db_dir = os.path.dirname(db_file)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

    Base.metadata.create_all(bind=engine)

    inspector = inspect(engine)
    if "evenements" in inspector.get_table_names() and CSV_PATH and os.path.exists(CSV_PATH):
        with engine.connect() as conn:
            count = conn.exec_driver_sql("SELECT COUNT(*) FROM evenements").scalar()
        if not count:
            df = pd.read_csv(CSV_PATH)
            df.to_sql("evenements", engine, if_exists="append", index=False)


def get_db():
    """Dependance FastAPI : fournit une session puis la referme."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
