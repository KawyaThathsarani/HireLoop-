from fastapi import FastAPI

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
