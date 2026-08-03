from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.enums import CommunicationStatus, CommunicationType
# use for API impurts and outputs


class CommunicationLogCreate(BaseModel):
    application_id: int
    message_type: CommunicationType = CommunicationType.EMAIL

    subject: str = Field(
        min_length=2,
        max_length=250,
    )

    body: str = Field(
        min_length=2,
    )

    status: CommunicationStatus = CommunicationStatus.SENT


class CommunicationLogResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    application_id: int
    message_type: CommunicationType
    subject: str
    body: str
    status: CommunicationStatus
    sent_at: datetime | None
    created_at: datetime
