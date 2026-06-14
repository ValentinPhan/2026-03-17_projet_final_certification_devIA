import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_IA_URL") or f"http://localhost:{os.getenv('API_IA_PORT')}/predict"
API_IA_URL = f"http://localhost:{os.getenv('API_IA_PORT')}"


# -----------------------------
# Configuration
# -----------------------------
# API_URL = os.getenv("API_IA_URL", "http://api:8000/predict")   # API IA FastAPI


st.set_page_config(
    page_title="Prédiction Gravité – Projet DevIA",
    page_icon="🚦",
    layout="centered"
)

st.title("🚦 Prédiction de la gravité d’un événement ferroviaire")
st.write("Cette application utilise un modèle IA exposé via une API FastAPI.")

# -----------------------------
# Formulaire utilisateur
# -----------------------------
st.subheader("📝 Saisir les caractéristiques de l’événement")

type_evenement = st.selectbox(
    "Type d'événement",
    ["collision", "incendie", "défaillance", "autre"]
)

departement = st.text_input("Département (ex : 69, 75, 44)")

exploitant = st.selectbox(
    "Exploitant",
    ["SNCF Réseau", "RATP", "Autre"]
)

nb_morts = st.number_input("Nombre de morts", min_value=0, step=1)
nb_blesses = st.number_input("Nombre de blessés", min_value=0, step=1)

# -----------------------------
# Appel API IA
# -----------------------------
if st.button("🔮 Prédire la gravité"):
    payload = {
        "type_evenement": type_evenement,
        "departement": departement,
        "exploitant": exploitant,
        "nb_morts": nb_morts,
        "nb_blesses": nb_blesses
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Gravité prédite : **{result['gravite_predite']}**")
            if result.get("proba"):
                st.info(f"Confiance du modèle : {result['proba']:.2f}")
        else:
            st.error(f"Erreur API : {response.text}")

    except Exception as e:
        st.error(f"Impossible de contacter l’API IA : {e}")
