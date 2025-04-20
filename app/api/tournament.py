from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Tournament, Player, TournamentParticipant
from app.api.schemas import tournament as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Beispiel-Endpunkt: Ping für Tournament-API
@router.get("/ping")
def ping():
    return {"status": "pong (tournament)"}

