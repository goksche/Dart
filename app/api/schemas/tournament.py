from pydantic import BaseModel
from typing import Optional, Literal
from datetime import date

class TournamentCreate(BaseModel):
    name: str
    type: Literal["spass", "wertung"]
    mode: Literal["liga", "ko", "gruppe"]
    date: Optional[date]
    is_ranked: bool = False

class TournamentOut(TournamentCreate):
    id: int

    class Config:
        from_attributes = True
