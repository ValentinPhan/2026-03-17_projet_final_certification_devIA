from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "evenements"

    id_evenement = Column(Integer, primary_key=True, index=True)
    date = Column(String)
    annee = Column(Integer)
    type_evenement = Column(String)
    gravite = Column(String)
    departement = Column(String)
    exploitant = Column(String)
    nb_morts = Column(Integer)
    nb_blesses = Column(Integer)
    cause_presumee = Column(String)
    contexte = Column(String)
    source = Column(String)

    class Config:
        orm_mode = True
