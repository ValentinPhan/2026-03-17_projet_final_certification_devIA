import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
import joblib

DATA_FILE = "data/evenements_1500.csv"
MODEL_FILE = "models/model.joblib"

def load_data():
    df = pd.read_csv(DATA_FILE)

    # Cible : gravité
    y = df["gravite"]

    # Features simples
    X = df[[
        "type_evenement",
        "departement",
        "exploitant",
        "nb_morts",
        "nb_blesses"
    ]]

    return X, y

def build_pipeline():
    categorical = ["type_evenement", "departement", "exploitant"]
    numeric = ["nb_morts", "nb_blesses"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
            ("num", "passthrough", numeric)
        ]
    )

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        random_state=42
    )

    pipeline = Pipeline([
        ("preprocess", preprocessor),
        ("model", model)
    ])

    return pipeline

def train():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    print("\n=== Rapport de performance ===")
    print(classification_report(y_test, y_pred))

    joblib.dump(pipeline, MODEL_FILE)
    print(f"\nModèle sauvegardé dans : {MODEL_FILE}")

if __name__ == "__main__":
    train()
