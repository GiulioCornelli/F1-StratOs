
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import models, schemas, auth
import os

app = FastAPI(title="F1 StratOS Authentication Module")

# Monta la cartella static per i file CSS/JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Endpoint per servire la pagina HTML principale
@app.get("/")
async def read_index():
    return FileResponse('static/index.html')

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user_data: schemas.UserRegister, db: Session = Depends(get_db)):
    existing_user = db.query(models.Utente).filter(models.Utente.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email già registrata")

    new_residenza = models.Residenza(
        paese=user_data.paese,
        regione=user_data.regione,
        citta=user_data.citta
    )
    db.add(new_residenza)
    db.commit()
    db.refresh(new_residenza)

    new_utente = models.Utente(
        nome=user_data.nome,
        cognome=user_data.cognome,
        email=user_data.email,
        id_privilegio=user_data.id_privilegio,
        id_residenza=new_residenza.id_residenza
    )
    db.add(new_utente)
    db.commit()
    db.refresh(new_utente)

    hashed_pwd = auth.get_password_hash(user_data.password)
    new_password_entry = models.Password(
        password_hash=hashed_pwd,
        id_utente=new_utente.id_utente
    )
    db.add(new_password_entry)
    db.commit()

    return {"message": "Utente registrato con successo", "id_utente": new_utente.id_utente}

@app.post("/login", response_model=schemas.LoginResponse)
def login_stalker(credentials: schemas.AdminLogin, db: Session = Depends(get_db)):
    user = db.query(models.Utente).filter(models.Utente.email == credentials.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenziali non valide (Utente non trovato)")

    pwd_entry = db.query(models.Password).filter(models.Password.id_utente == user.id_utente).first()
    if not pwd_entry:
        raise HTTPException(status_code=500, detail="Errore integrità dati: Password non trovata")

    if not auth.verify_password(credentials.password, pwd_entry.password_hash):
        raise HTTPException(status_code=401, detail="Credenziali non valide (Password errata)")

    return {
        "message": "Login effettuato con successo",
        "id_utente": user.id_utente,
        "nome": user.nome
    }

@app.post("/init-privileges")
def init_privileges(db: Session = Depends(get_db)):
    existing = db.query(models.Privilegio).first()
    if not existing:
        p = models.Privilegio(nome="Admin", descrizione="Amministratore di sistema")
        db.add(p)
        db.commit()
        return {"message": "Privilegio 'Admin' creato"}
    return {"message": "Privilegi già esistenti"}
