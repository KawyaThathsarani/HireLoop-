from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.enums import ApplicationStage


class StageHistoryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    application_id: int
    old_stage: ApplicationStage
    new_stage: ApplicationStage
    changed_at: datetime
