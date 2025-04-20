from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nickname = Column(String)
    email = Column(String, unique=True, index=True)

from sqlalchemy import Column, Integer, String, Boolean, Date

class Tournament(Base):
    __tablename__ = "tournaments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)  # "spass", "wertung"
    mode = Column(String, nullable=False)  # "liga", "ko", "gruppe"
    date = Column(Date)
    is_ranked = Column(Boolean, default=False)

from sqlalchemy import ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship

class TournamentParticipant(Base):
    __tablename__ = "tournament_participants"

    id = Column(Integer, primary_key=True, index=True)
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    player_id = Column(Integer, ForeignKey("players.id"))
    is_seeded = Column(Boolean, default=False)

    tournament = relationship("Tournament", backref="participants")
    player = relationship("Player")

    __table_args__ = (
        UniqueConstraint("tournament_id", "player_id", name="_tournament_player_uc"),
    )
