
from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    nome: str
    cognome: str
    email: EmailStr
    paese: str
    regione: str
    citta: str
    password: str
    id_privilegio: int = 1 

class AdminLogin(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    message: str
    id_utente: int
    nome: str
