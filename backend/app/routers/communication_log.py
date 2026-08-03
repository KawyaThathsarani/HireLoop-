from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.enums import CommunicationStatus
from app.models.application import Application
from app.models.communication_log import CommunicationLog
from app.schemas.communication_log import CommunicationLogCreate, CommunicationLogResponse

router = APIRouter(
    prefix="/api/communication-logs",
    tags=["Communication Logs"]
)


@router.post(
    "",
    response_model=CommunicationLogResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_communication_log(
    log_data: CommunicationLogCreate,
    db: Session = Depends(get_db),
) -> CommunicationLog:
    application = db.get(
        Application,
        log_data.application_id,
    )

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application not found.",
        )

    sent_at = None

    if log_data.status == CommunicationStatus.SENT:
        sent_at = datetime.now(timezone.utc)  # Coordinated Universal Time
        application.last_communication_at = sent_at

    communication_log = CommunicationLog(
        application_id=log_data.application_id,
        message_type=log_data.message_type.value,
        subject=log_data.subject,
        body=log_data.body,
        status=log_data.status.value,
        sent_at=sent_at,
    )

    db.add(communication_log)
    db.commit()
    db.refresh(communication_log)

    return communication_log


@router.get(
    "/application/{application_id}",
    response_model=list[CommunicationLogResponse],
)
def get_communication_log_by_application(
    application_id: int,
    db: Session = Depends(get_db),
) -> list[CommunicationLog]:
    application = db.get(
        Application,
        application_id,
    )

    if application is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Application is not fouund.",
        )

    logs = db.scalars(
        select(CommunicationLog).where(CommunicationLog.application_id ==
                                       application_id).order_by(CommunicationLog.created_at)

    ).all()

    return list(logs)
