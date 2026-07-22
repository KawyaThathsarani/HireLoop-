from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from app.enums import JobStatus


class JobCreate(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=200,
    )

    department: str = Field(
        min_length=2,
        max_length=200,
    )
    status: JobStatus = JobStatus.OPEN


class JobResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    title: str
    department: str
    status: JobStatus
    created_at: datetime
