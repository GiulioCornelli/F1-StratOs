# librerie esterne
from fastapi import FastAPI

# librerie custom
from .routes import routerDriver, routerMeeting

app = FastAPI()

app.include_router(routerDriver)
app.include_router(routerMeeting)
