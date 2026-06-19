import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from app.models import Base

# Charger les variables d'environnement
load_dotenv()

# Récupérer l'URL de la base
DB_URL = os.getenv("DB_URL")

if DB_URL is None:
    raise ValueError("❌ La variable d'environnement DB_URL est absente du fichier .env")

# Créer l'engine SQLAlchemy
engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

def init_database():
    print("📌 Création des tables…")
    Base.metadata.create_all(bind=engine)

    # Charger le CSV
    csv_path = os.path.join("data", "evenements_1500.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"❌ Fichier CSV introuvable : {csv_path}")

    print("📌 Chargement du CSV dans la base…")
    df = pd.read_csv(csv_path)

    # Insérer dans la table
    with engine.begin() as conn:
        # Vérifier si la table est vide
        result = conn.execute(text("SELECT COUNT(*) FROM evenements"))
        count = result.scalar()

        if count == 0:
            df.to_sql("evenements", conn, if_exists="append", index=False)
            print("✅ Données insérées dans la table 'evenements'")
        else:
            print("ℹ️ La table 'evenements' contient déjà des données, aucune insertion effectuée.")

    print("🎉 Base initialisée avec succès !")

if __name__ == "__main__":
    init_database()
