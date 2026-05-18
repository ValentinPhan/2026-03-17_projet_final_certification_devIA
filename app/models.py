from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    id_evenement: int
    date: str
    annee: int
    type_evenement: str
    gravite: str
    departement: str
    exploitant: str
    nb_morts: Optional[int]
    nb_blesses: Optional[int]
    cause_presumee: Optional[str]
    contexte: Optional[str]
    source: Optional[str]

    class Config:
        orm_mode = True
