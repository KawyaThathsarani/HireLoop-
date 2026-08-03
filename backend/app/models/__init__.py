from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job
from app.models.stage_history import StageHistory
from app.models.communication_log import CommunicationLog

__all__ = [
    "Application",
    "Candidate",
    "Job",
    "StageHistory",
    "CommunicationLog"
]
# access the classes of the each model database class
# helps to find the classes in the new table creation
