from fastapi import FastAPI
# import our database session creator. This lets main.py talk to PostgreSQL
from sqlalchemy import text

# import database session creator
from app.database import SessionLocal, Base, engine
from app.models import Application, Candidate, Job
from app.routers import application, candidate, communication_log, job, email

app = FastAPI(
    title="HireLoop API",
    description="Candidate communication and recruitment closure system",
    version="1.0"
)

# to create base to know about all the database models , and engine to connect to PostgreSQL.
Base.metadata.create_all(bind=engine)

# home api route creation when we get in to the home it shows this message
app.include_router(candidate.router)
app.include_router(job.router)
app.include_router(application.router)
app.include_router(communication_log.router)
app.include_router(email.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to HireLoop API!"}


@app.get("/health")  # health check route creation
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


@app.get("/health/database")
def database_health_check() -> dict[str, str]:
    with SessionLocal() as db:
        db.execute(text("SELECT 1"))

    return {
        "status": "Healthy",
        "database": "connected",
    }
