# librerie esterne
from fastapi import FastAPI
from contextlib import asynccontextmanager
# import httpx
# from httpx import ConnectTimeout, ReadTimeout
# import asyncio


# librerie custom
<<<<<<< HEAD
from .routes import routerDriver, routerMeeting
from src.logo import GATEWAY_BANNER,F1_STRATOS_EXIT,BOLD, RESET, GREEN
=======
from .routes import routerDriver
from src.logo import GATEWAY_BANNER,F1_STRATOS_EXIT
>>>>>>> main



@asynccontextmanager
async def lifespan(app: FastAPI):
    print(GATEWAY_BANNER)
    
    
    yield
    print(F1_STRATOS_EXIT)

   



app = FastAPI(lifespan=lifespan)

# --- Rotte ---
app.include_router(routerDriver)
