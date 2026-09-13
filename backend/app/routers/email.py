from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job
from app.schemas.email import (
    EmailPreviewRequest,
    EmailPreviewResponse,
)

from app. services.email_template_service import generate_email_preview

router = APIRouter(
    prefix="/api/emails",
    tags=["Emails"],
)


@router.post(
    "/preview",
    response_model=EmailPreviewResponse,
)
def preview_email(
    email_data: EmailPreviewRequest,
    db: Session = Depends(get_db),
):
    application = db.get(
        Application, email_data.application_id,
    )

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found.",
        )

    candidate = db.get(
        Candidate,
        application.candidate_id,
    )

    if candidate is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Candidate not found.",
        )

    job = db.get(
        Job,
        application.job_id,
    )

    if job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found.",
        )

    return generate_email_preview(
        application=application,
        candidate=candidate,
        job=job,
        template_type=email_data.template_type,
        interview_date=email_data.interview_date,
        notes=email_data.notes,
    )
