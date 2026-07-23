from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.enums import ApplicationStage, ApplicationStatus


class ApplicationCreate(BaseModel):
    candidate_id: int
    job_id: int

    current_stage: ApplicationStage = (
        ApplicationStage.APPLIED
    )

    status: ApplicationStatus = (
        ApplicationStatus.ACTIVE
    )


class ApplicationStageUpdate(BaseModel):
    current_stage: ApplicationStage


class ApplicationResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    candidate_id: int
    job_id: int
    current_stage: ApplicationStage
    status: ApplicationStatus
    last_communication_at: datetime | None
    created_at: datetime
    updated_at: datetime
