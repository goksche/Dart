# app/api/tournament.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models import Tournament
from app.api.schemas import tournament as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/ping")
def ping():
    return {"status": "pong (tournament)"}

@router.post("/", response_model=schema.TournamentOut)
def create_tournament(t: schema.TournamentCreate, db: Session = Depends(get_db)):
    new_tournament = Tournament(**t.dict())
    db.add(new_tournament)
    db.commit()
    db.refresh(new_tournament)
    return new_tournament

