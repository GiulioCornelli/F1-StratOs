
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Privilegio(Base):
    __tablename__ = "privilegi"
    id_privilegio = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descrizione = Column(String, nullable=True)

class Residenza(Base):
    __tablename__ = "residenza"
    id_residenza = Column(Integer, primary_key=True, index=True)
    paese = Column(String, nullable=False)
    regione = Column(String, nullable=False)
    citta = Column(String, nullable=False)

class Utente(Base):
    __tablename__ = "utenti"
    id_utente = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cognome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    id_privilegio = Column(Integer, ForeignKey("privilegi.id_privilegio"))
    id_residenza = Column(Integer, ForeignKey("residenza.id_residenza"))

    privilegio = relationship("Privilegio")
    residenza = relationship("Residenza")

class Password(Base):
    __tablename__ = "password"
    id_password = Column(Integer, primary_key=True, index=True)
    password_hash = Column(String, nullable=False)
    id_utente = Column(Integer, ForeignKey("utenti.id_utente"), nullable=False)
