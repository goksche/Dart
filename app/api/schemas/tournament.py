from pydantic import BaseModel
from typing import Optional, Literal, List
from datetime import date

# Turnier-Erstellung
class TournamentCreate(BaseModel):
    name: str
    type: Literal["spass", "wertung"]
    mode: Literal["liga", "ko", "gruppe"]
    date: Optional[date]
    is_ranked: bool = False

# Turnier-Ausgabe
class TournamentOut(TournamentCreate):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2

# Spieler zu Turnier hinzufügen
class TournamentAddPlayer(BaseModel):
    player_id: int
    is_seeded: bool = False

# Teilnehmer-Ausgabe
class TournamentParticipantOut(BaseModel):
    player_id: int
    player_name: str
    is_seeded: bool

    class Config:
        from_attributes = True
