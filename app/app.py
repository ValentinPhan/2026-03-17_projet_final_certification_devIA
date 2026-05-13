import streamlit as st
import pandas as pd
import joblib
import sklearn
metadata = {
    "model": model,
    "sklearn_version": sklearn.__version__
}

joblib.dump(metadata, "model_with_meta.joblib")
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "rf_gravite_pipeline.joblib"

# --- Chargement du modèle (mis en cache pour ne pas recharger à chaque interaction)
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# --- Interface utilisateur
st.title("🚆 Prédiction de la gravité d'incidents ferroviaires")
st.markdown("Renseignez les caractéristiques de l'événement pour obtenir une prédiction.")

# --- Formulaire de saisie
col1, col2 = st.columns(2)

with col1:
    annee = st.slider("Année", 2010, 2024, 2020)
    type_evenement = st.selectbox("Type d'événement", 
        ["collision", "deraillement", "PN", "incendie", 
         "incident_materiel", "acte_malveillance"])
    exploitant = st.selectbox("Exploitant", 
        ["SNCF Réseau", "SNCF Voyageurs", "RATP"])

with col2:
    departement = st.number_input("Département", 1, 95, 69)
    cause_presumee = st.selectbox("Cause présumée", 
        ["erreur_humaine", "defaillance_materiel", "defaut_infrastructure",
         "obstacle_PN", "non_respect_signalisation", "excès_vitesse",
         "incendie_bord", "acte_malveillance", "vol_cable", 
         "jet_de_projectiles", "defaillance_freinage", "defaillance_signalisation"])
    contexte = st.selectbox("Contexte", 
        ["circulation_commerciale", "PN", "maintenance", "travaux", "essais"])

source = st.selectbox("Source", ["EPSF_synthese", "SNCF_rapport", "BEATT_rapport"])

# --- Prédiction
if st.button("Prédire la gravité"):
    input_df = pd.DataFrame([{
        "annee": annee, "type_evenement": type_evenement,
        "exploitant": exploitant, "departement": departement,
        "cause_presumee": cause_presumee, "contexte": contexte,
        "source": source
    }])
    
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]
    
    # ↓ ICI — remplace l'ancien label_map et l'ancien st.bar_chart
    label_map = {
        0: "Mineur", 1: "Significatif", 2: "Grave",
        "mineur": "Mineur", "significatif": "Significatif", "grave": "Grave"
    }
    st.success(f"Gravité prédite : **{label_map[prediction]}**")
    
    classes = model.classes_  # ← récupère les classes du modèle
    proba_df = pd.DataFrame(proba, index=classes, columns=["Probabilité"])
    st.bar_chart(proba_df)  # ← remplace l'ancien st.bar_chart