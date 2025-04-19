from pydantic import BaseModel, EmailStr
from typing import Optional

class PlayerCreate(BaseModel):
    name: str
    nickname: Optional[str] = None
    email: Optional[EmailStr] = None

class PlayerUpdate(PlayerCreate):
    pass

class PlayerOut(PlayerCreate):
    id: int

    class Config:
        orm_mode = True
