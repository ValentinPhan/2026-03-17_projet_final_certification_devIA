MCD
Entité : Événement  
Attributs :

id_evenement (PK)

date

annee

type_evenement

gravite

departement

exploitant

nb_morts

nb_blesses

cause_presumee

contexte

source

MLD

EVENEMENTS(
  id_evenement INT PRIMARY KEY,
  date DATE,
  annee INT,
  type_evenement TEXT,
  gravite TEXT,
  departement TEXT,
  exploitant TEXT,
  nb_morts INT,
  nb_blesses INT,
  cause_presumee TEXT,
  contexte TEXT,
  source TEXT
)
