# routers keep the API end points
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateResponse

router = APIRouter(
    # api endpoints starts like this when we call "" in the below of the code
    prefix="/api/candidates",
    tags=["Candidates"],
)


@router.post(
    "",  # api will be like POST/api/candidates
    response_model=CandidateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_candidate(
    candidate_data: CandidateCreate,
    # dependancy injection fast api give this function what it needs
    db: Session = Depends(get_db),
) -> Candidate:
    candidate_email = str(candidate_data.email)

    existing_candidate = db.scalar(
        select(Candidate).where(
            Candidate.email == candidate_email
        )
    )

    if existing_candidate:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Candidate email already exist"
        )

    candidate = Candidate(
        name=candidate_data.name,
        email=candidate_email,
        phone=candidate_data.phone,
    )

    db.add(candidate)  # db means the object name (database session object)
    db.commit()
    db.refresh(candidate)

    return candidate


@router.get(
    "",
    response_model=list[CandidateResponse],
)
def get_candidates(
    db: Session = Depends(get_db),
) -> list[Candidate]:  # can get the return type as a list of candidate names and other details with like a order of id numebrs
    candidates = db.scalars(  # scalars give many results if we use scalar it only give one result like emil checking process
        select(Candidate).order_by(Candidate.id)
    ).all()  # give all matching numbers results as a list

    return list(candidates)
