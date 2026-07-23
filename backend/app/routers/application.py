from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationResponse, ApplicationStageUpdate
from app.models.candidate import Candidate
from app.models.job import Job
from app.enums import ApplicationStage, ApplicationStatus

router = APIRouter(
    prefix="/api/applications",
    tags=["Applications"],
)


@router.post(
    "",
    response_model=ApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_application(
    application_data: ApplicationCreate,
    db: Session = Depends(get_db),
) -> Application:
    candidate = db.get(
        Candidate, application_data.candidate_id,
    )

    job = db.get(
        Job,
        application_data.job_id,
    )

    application = Application(
        candidate_id=application_data.candidate_id,
        job_id=application_data.job_id,
        current_stage=application_data.current_stage.value,
        status=application_data.status.value,
    )

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found.",
        )

    db.add(application)
    db.commit()
    db.refresh(application)

    return application


@router.get(
    "",
    response_model=list[ApplicationResponse],
)
def get_applications(
    db: Session = Depends(get_db),
) -> list[Application]:
    applications = db.scalars(
        select(Application).order_by(Application.id)
    ).all()

    return list(applications)


@router.patch(
    "/{application_id}/stage",
    response_model=ApplicationResponse,
)
def update_application_stage(
    # application id is comes from the url(path paarameter)
    application_id: int,
    stage_data: ApplicationStageUpdate,
    db: Session = Depends(get_db)
) -> Application:
    application = db.get(
        Application,
        application_id,
    )

    new_stage = stage_data.current_stage
    application.current_stage = new_stage.value

    if new_stage == ApplicationStage.SELECTED:
        application.status = ApplicationStatus.SELECTED.value

    elif new_stage == ApplicationStage.REJECTED:
        application.status = ApplicationStage.REJECTED.value

    else:
        application.status = ApplicationStatus.ACTIVE.value

    db.commit()
    db.refresh(application)

    return application
