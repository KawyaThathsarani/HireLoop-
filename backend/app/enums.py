from enum import Enum


class JobStatus(str, Enum):
    OPEN = "OPEN"
    CLOSE = "CLOSED"


class ApplicationStage(str, Enum):
    APPLIED = "APPLIED"
    CV_SCREENING = "CV_SCREENING"
    HR_INTERVIEW = "HR_INTERVIEW"
    TECHNICAL_INTERVIEW = "TECHNICAL_INTERVIEW"
    FINAL_INTERVIEW = "FINAL_INTERVIEW"
    SELECTED = "SELECTED"
    REJECTED = "REJECTED"


class ApplicationStatus(str, Enum):
    ACTIVE = "ACTIVE"
    SELECTED = "SELECTED"
    REJECTED = "REJECTED"
    WITHDRAWN = "WITHDRAWN"


class CommunicationType(str, Enum):
    EMAIL = "EMAIL",
    PHONE = "PHONE",
    NOTE = "NOTE"


class CommunicationStatus(str, Enum):
    DRAFT = "DRAFT",
    SENT = "SENT",
    FAILED = "FAILED"
