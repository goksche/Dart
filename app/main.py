# app/main.py
from fastapi import FastAPI
from app.api import player
from app.core.settings import settings
from app.db.models import Base
from app.db.session import engine

app = FastAPI(title="Dartverein API")

# DB-Tabellen erzeugen
Base.metadata.create_all(bind=engine)

# Router einbinden
app.include_router(player.router, prefix="/player", tags=["Player"])

@app.get("/ping")
def ping():
    return {"status": "pong"}
