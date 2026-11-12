from fastapi import FastAPI
from .database import Base, engine
from .models import Incident
from .routers.incidents import router as incidents_router

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(incidents_router)


@app.get("/")
def home():
    return {"message" : "Incident manager app is running."}

