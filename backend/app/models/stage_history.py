from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class StageHistory(Base):
    __tablename__ = "stage_history"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("applications.id"),
        nullable=False,
        index=True,
    )

    old_stage: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    new_stage: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    changed_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
