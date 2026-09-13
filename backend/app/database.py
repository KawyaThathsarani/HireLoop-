import os
from collections.abc import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

load_dotenv()

Database_URL = os.getenv("DATABASE_URL")
if not Database_URL:
    raise RuntimeError(
        "DATABASE_URL is not confugured. Please set the DATABASE_URL environment variable in your .env file."
    )

engine = create_engine(Database_URL, echo=True)
# create sqlAlchemy ddatabase engine,echo true prints the sql in terminal,

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)
# session active conversions with the database database session is used to perform database work.


class Base(DeclarativeBase):
    pass
# All the database models will inherit from this base class, like ooop inheritance


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create database FastAPI will use this function to provide a database session to API routes.
# Open database session
#   ↓
# Use it inside API function
#   ↓
# Close it safely
