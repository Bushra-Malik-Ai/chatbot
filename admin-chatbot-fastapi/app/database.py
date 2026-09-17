"""
Database setup — SQLite via SQLAlchemy.
Swap SQLALCHEMY_DATABASE_URL for a Postgres/MySQL URL in production;
nothing else in the app needs to change.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./directory.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # needed only for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """FastAPI dependency — yields a DB session per request and closes it after."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        
