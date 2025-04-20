# app/db/models.py
from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nickname = Column(String)
    email = Column(String, unique=True, index=True)

class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # spass / wertung
    mode = Column(String, nullable=False)  # liga / ko / gruppe
    date = Column(Date)
    is_ranked = Column(Boolean, default=False)
