#librerie esterne
from fastapi import FastAPI

#librerie custom
from .routes.routesDrivers import routerDriver

app = FastAPI()

app.include_router(routerDriver)