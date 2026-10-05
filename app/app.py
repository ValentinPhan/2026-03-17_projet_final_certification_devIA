import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# En Docker : API_IA_URL=http://api_ia:8000/predict ; en local : localhost:API_IA_PORT
API_URL = os.getenv("API_IA_URL") or f"http://localhost:{os.getenv('API_IA_PORT', '8000')}/predict"


# -----------------------------
# Configuration
# -----------------------------
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
    # Categories connues du modele (cf. data/evenements_1500.csv)
    ["collision", "deraillement", "incendie", "incident_materiel", "PN", "acte_malveillance"]
)

departement = st.text_input("Département (ex : 69, 75, 44)").strip()

exploitant = st.selectbox(
    "Exploitant",
    ["SNCF Réseau", "SNCF Voyageurs", "RATP"]
)

nb_morts = st.number_input("Nombre de morts", min_value=0, step=1)
nb_blesses = st.number_input("Nombre de blessés", min_value=0, step=1)

# -----------------------------
# Appel API IA
# -----------------------------
if st.button("🔮 Prédire la gravité"):
    if not departement:
        st.warning("Veuillez saisir un département.")
        st.stop()

    payload = {
        "type_evenement": type_evenement,
        "departement": departement,
        "exploitant": exploitant,
        "nb_morts": int(nb_morts),
        "nb_blesses": int(nb_blesses)
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=10)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Gravité prédite : **{result['gravite_predite']}**")
            if result.get("proba") is not None:
                st.info(f"Confiance du modèle : {result['proba']:.2f}")
        else:
            st.error(f"Erreur API : {response.text}")

    except Exception as e:
        st.error(f"Impossible de contacter l’API IA : {e}")
