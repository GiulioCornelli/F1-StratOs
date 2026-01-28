#librerie esterne
from fastapi import FastAPI
from contextlib import asynccontextmanager


#librerie custom
from .routes.routesDrivers import routerDriver
from src.logo import MONGO_STALKER_BANNER,F1_STRATOS_EXIT, SHUTDOWN_BANNER, BOLD, RESET, GREEN
from .database.database import MongoManager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Stampiamo il banner importato
    print(MONGO_STALKER_BANNER)
    print(f"{BOLD}Inizializzazione Lifespan...{RESET}")
    yield
    print(F1_STRATOS_EXIT)
    print(f"{GREEN}✔{RESET} {BOLD}Connection MongoDB Closed Successfully. Bye! {RESET}") 
    MongoManager.close_connection()

app = FastAPI(lifespan=lifespan)

app.include_router(routerDriver)