# librerie esterne
from fastapi import FastAPI
from contextlib import asynccontextmanager
# import httpx
# from httpx import ConnectTimeout, ReadTimeout
# import asyncio  
from fastapi.middleware.cors import CORSMiddleware


# librerie custom
from .routes.routesDriver import routerDriver
from .routes.routesAuth import routerAuth
from src.logo import GATEWAY_BANNER,F1_STRATOS_EXIT



@asynccontextmanager
async def lifespan(app: FastAPI):
    print(GATEWAY_BANNER)
    yield
    print(F1_STRATOS_EXIT)

   



app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # L'URL del tuo Frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Rotte ---
app.include_router(routerDriver)
app.include_router(routerAuth)
