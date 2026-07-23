from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.enums import ApplicationStage, ApplicationStatus


class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("candidates.id"),  # table name and table column
        nullable=False,
        index=True,
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("jobs.id"),  # table name and table column
        nullable=False,
        index=True,
    )

    current_stage: Mapped[str] = mapped_column(
        String(50),
        default=ApplicationStage.APPLIED.value,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        # when open a job application it automatically by default it is be like ACTIVE
        default=ApplicationStatus.ACTIVE.value,
        nullable=False,
    )

    last_communication_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
