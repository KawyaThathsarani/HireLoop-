from fastapi import FastAPI
# import our database session creator. This lets main.py talk to PostgreSQL
from sqlalchemy import text

from app.database import SessionLocal

app = FastAPI(
    title="HireLoop API",
    description="Candidate communicationa and recruitment closure system",
    version="1.0"
)


# home api route creation when we get in to the home it shows this message
@app.get("/")
def root() -> dict:
    return {"message": "Welcome to HireLoop API!"}


@app.get("/health")  # health check route creation
def health_check() -> dict:
    return {"status": "healthy"}


@app.get("/health/database")
def database_health_check() -> dict[str, str]:
    with SessionLocal() as db:
        db.execute(text("SELECT 1"))

    return {
        "status": "Healthy",
        "database": "connected",
    }
