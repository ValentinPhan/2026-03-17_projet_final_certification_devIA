import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from pathlib import Path
import joblib

# -----------------------------
# Chemins
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[0]
DATA_FILE = BASE_DIR / "data" / "evenements_1500.csv"
MODEL_FILE = BASE_DIR / "models" / "model.joblib"

# -----------------------------
# Chargement des données
# -----------------------------
def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Fichier introuvable : {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)

    # Cible
    y = df["gravite"]

    # Features
    X = df[[
        "type_evenement",
        "departement",
        "exploitant",
        "nb_morts",
        "nb_blesses"
    ]]

    return X, y

# -----------------------------
# Construction du pipeline ML
# -----------------------------
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
        n_estimators=300,
        max_depth=10,
        random_state=42
    )

    pipeline = Pipeline([
        ("preprocess", preprocessor),
        ("model", model)
    ])

    return pipeline

# -----------------------------
# Entraînement
# -----------------------------
def train():
    print("📥 Chargement des données…")
    X, y = load_data()

    print("✂️ Split train/test…")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print("🧠 Construction du pipeline…")
    pipeline = build_pipeline()

    print("🚀 Entraînement du modèle…")
    pipeline.fit(X_train, y_train)

    print("\n📊 Rapport de performance :")
    y_pred = pipeline.predict(X_test)
    print(classification_report(y_test, y_pred))

    print(f"\n💾 Sauvegarde du modèle dans : {MODEL_FILE}")
    MODEL_FILE.parent.mkdir(exist_ok=True)
    joblib.dump(pipeline, MODEL_FILE)

    print("✅ Modèle entraîné et sauvegardé avec succès.")

if __name__ == "__main__":
    train()
