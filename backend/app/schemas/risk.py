from pydantic import BaseModel

from app.enums import CommunicationRiskLevel


class CommunicationRiskResponse(BaseModel):
    application_id: int
    risk_level: CommunicationRiskLevel
    days_since_last_communication: int | None
    message: str
