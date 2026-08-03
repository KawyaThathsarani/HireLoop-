from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.enums import CommunicationStatus, CommunicationType

# preventing candidate ghosting and tracking candidate communication.


class CommunicationLog(Base):
    __tablename__ = "communication_logs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id"),
        nullable=False,
        index=True,
    )

    message_type: Mapped[str] = mapped_column(  # can be email, phone call, note
        String(30),
        default=CommunicationType.EMAIL.value,
        nullable=False,
    )

    subject: Mapped[str] = mapped_column(  # email subject or short title are strore in here
        String(250),
        nullable=False,
    )

    body: Mapped[str] = mapped_column(  # Actual message content.
        Text,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(  # Whether it is DRAFT, SENT, or FAILED the current status of the communication
        String(30),
        default=CommunicationStatus.DRAFT.value,
        nullable=False,
    )

    sent_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
