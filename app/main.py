from fastapi import FastAPI
from .database import Base, engine
from .models import Incident

Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
def home():
    return {"message" : "Incident manager app is running."}