from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={"check_same_thread": False}  # Nur für SQLite nötig
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
