# schemas for request response structure creating purpose
# mainly use for the APIs
from datetime import datetime
from pydanthic import BaseModel, ConfigDict, EmailStr, Field
# Pydanthic used for data validation and serialiation


class CandidateCreate(BaseModel):  # controls what the API sends back.
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: EmailStr  # This checks whether the email looks like a real email.

    phone: str | None = Feild(
        default=None,
        max_length=30,
    )


# manage what the API sends bach like response.
class CandidateResponse(BaseModel):
    model_config = ConfigDict(  # This allows Pydantic(use for data visualization and serialoization) to read data from SQLAlchemy objects.
        from_attributes=True
    )

    id: int
    name: str
    email = EmailStr
    phone: str | None
    created_at: datetime
