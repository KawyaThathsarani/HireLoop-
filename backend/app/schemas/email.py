from pydantic import BaseModel, Field
from app.enums import EmailTemplateType


class EmailPreviewRequest(BaseModel):
    application_id: int
    template_type: EmailTemplateType
    interview_date: str | None = Field(
        default=None,
        max_length=100,
    )

    notes: str | None = Field(
        default=None,
        max_length=500,
    )


class EmailPreviewResponse(BaseModel):
    application_id: str
    job_title: str
    template_type: EmailTemplateType
    candidate_name: str
    subject: str
    body: str
