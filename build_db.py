"""Genere data/events.db a partir de data/evenements_1500.csv.

Script autonome : utilise uniquement la bibliotheque standard Python
(sqlite3 + csv). Aucune dependance (pas besoin du venv, ni de pandas,
ni de SQLAlchemy). Chemins calcules a partir de l'emplacement du fichier,
donc executable depuis n'importe quel dossier :

    python build_db.py
"""
import csv
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "data", "evenements_1500.csv")
DB_PATH = os.path.join(BASE_DIR, "data", "events.db")

COLUMNS = [
    "id_evenement", "date", "annee", "type_evenement", "gravite",
    "departement", "exploitant", "nb_morts", "nb_blesses",
    "cause_presumee", "contexte", "source",
]

CREATE_SQL = """
CREATE TABLE evenements (
    id_evenement   INTEGER PRIMARY KEY,
    date           TEXT,
    annee          INTEGER,
    type_evenement TEXT,
    gravite        TEXT,
    departement    TEXT,
    exploitant     TEXT,
    nb_morts       INTEGER,
    nb_blesses     INTEGER,
    cause_presumee TEXT,
    contexte       TEXT,
    source         TEXT
)
"""


def main():
    if not os.path.exists(CSV_PATH):
        raise FileNotFoundError(f"CSV introuvable : {CSV_PATH}")

    # On repart d'une base propre
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(CREATE_SQL)

    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = [tuple(row[c] for c in COLUMNS) for row in reader]

    placeholders = ",".join(["?"] * len(COLUMNS))
    cur.executemany(f"INSERT INTO evenements VALUES ({placeholders})", rows)
    con.commit()

    total = cur.execute("SELECT COUNT(*) FROM evenements").fetchone()[0]
    con.close()
    print(f"OK : {total} lignes ecrites dans {DB_PATH}")


if __name__ == "__main__":
    main()
