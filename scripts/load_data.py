import pandas as pd
import sqlalchemy
import argparse

def load_data(db_url: str, file: str, table: str = "evenements"):
    engine = sqlalchemy.create_engine(db_url)

    df = pd.read_csv(file)
    df.to_sql(table, engine, if_exists="replace", index=False)

    print(f"Import terminé : {len(df)} lignes dans la table '{table}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--db-url", required=True)
    parser.add_argument("--file", required=True)
    parser.add_argument("--table", default="evenements")
    args = parser.parse_args()

    load_data(args.db_url, args.file, args.table)
