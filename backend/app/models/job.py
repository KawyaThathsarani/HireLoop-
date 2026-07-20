from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base
from app.enums import JobStatus


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    department: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default=JobStatus.OPEN.value,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
