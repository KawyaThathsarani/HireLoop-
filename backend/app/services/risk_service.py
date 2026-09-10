from datetime import datetime, timezone

from app.enums import CommunicationRiskLevel
from app.models.application import Application


def calculate_communication_risk(
    application: Application,
) -> dict:
    if application.last_communication_at is None:
        return {
            "application_id": application.id,
            "risk_level": CommunicationRiskLevel.HIGH,
            "days_since_last_communication": None,
            "message": "Candidate has not been contacted yet.",
        }

    now = datetime.now(timezone.utc)

    last_contact = application.last_communication_at

    if last_contact.tzinfo is None:
        last_contact = last_contact.replace(tzinfo=timezone.utc)

    days_since_last_communication = (
        now - last_contact
    ).days

    if days_since_last_communication <= 3:
        risk_level = CommunicationRiskLevel.LOW
        message = "Candidate was contacted recently."

    elif days_since_last_communication <= 7:
        risk_level = CommunicationRiskLevel.MEDIUM
        message = (
            "Candidate has not been contacted for a few days."
        )

    else:
        risk_level = CommunicationRiskLevel.HIGH
        message = (
            "Candidate has not been contacted for too long."
        )

    return {
        "application_id": application.id,
        "risk_level": risk_level,
        "days_since_last_communication": days_since_last_communication,
        "message": message,
    }
