import os
import sys

# Permet d'executer le script directement (python scripts/init_db.py)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from app.models import Base

load_dotenv()

DB_URL = os.getenv("DB_URL")
if DB_URL is None:
    raise ValueError("La variable d'environnement DB_URL est absente du fichier .env")

# S'assurer que le dossier de la base SQLite existe
if DB_URL.startswith("sqlite:///"):
    db_file = DB_URL.replace("sqlite:///", "", 1)
    db_dir = os.path.dirname(db_file)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

connect_args = {"check_same_thread": False} if DB_URL.startswith("sqlite") else {}
engine = create_engine(DB_URL, connect_args=connect_args)


def init_database():
    print("Creation des tables...")
    Base.metadata.create_all(bind=engine)

    csv_path = os.getenv("CSV_EVENTS_PATH", os.path.join("data", "evenements_1500.csv"))
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Fichier CSV introuvable : {csv_path}")

    print("Chargement du CSV dans la base...")
    df = pd.read_csv(csv_path)

    with engine.begin() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM evenements")).scalar()
        if count == 0:
            df.to_sql("evenements", conn, if_exists="append", index=False)
            print(f"{len(df)} lignes inserees dans la table 'evenements'")
        else:
            print("La table contient deja des donnees, aucune insertion.")

    print("Base initialisee avec succes !")


if __name__ == "__main__":
    init_database()
