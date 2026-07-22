# routers keep the API end points
from fastapi import APIRouter, depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateResponse

router = APIRouter(
    prefix="/api/candidates",
    tags=["Candidates"],
)


@router.post(
    "",
    response_model=CandidateResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_candidate(
    candidate_data: CandidateCreate,
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

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate


@router.get(
    "",
    response_model=list[CandidateResponse],
)
def get_candidates(
    db: Session = Depends(get_db),
) -> list[Candidate]:
    candidates = db.scalars(
        select(Candidate).order_by(Candidate.id)
    ).all()

    return list(candidates)
