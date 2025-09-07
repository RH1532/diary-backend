from fastapi import FastAPI
from .db import Base, engine
from .routers import notes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Daily Notes API")

app.include_router(notes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Daily Notes API"}
