from app.enums import EmailTemplateType
from app.models.application import Application
from app.models.candidate import Candidate
from app.models.job import Job


def generate_email_preview(
        application: Application,
        candidate: Candidate,
        job: Job,
        template_type: EmailTemplateType,
        interview_date: str | None = None,
        notes: str | None = None,
) -> dict:
    candidate_first_name = candidate.name.split()[0]

    if template_type == EmailTemplateType.APPLICATION_RECIEVED:
        subject = f"Application Received-{job.title}"

        body = (
            f"Dear {candidate_first_name},\n\n"
            f"thankyou for applying for the {job.title} position at our company. We have received your application and our team will review it shortly.\n\n"
            f"we will contact you if you are shortlisted for the next stage.\n\n"
            f"Best regards,\n"
            f"The Hiring Team"
        )
    elif template_type == EmailTemplateType.INTERVIEW_INVITATION:
        subject = f"Interview Invitation-{job.title}"

        body = (
            f"Dear {candidate_first_name},\n\n"
            f"We are pleased to inform you that you have been shortlisted for an interview for the {job.title} position at our company.\n\n"
            f"Interview Date: {interview_date}\n"
            f"Please confirm your availability for the interview by replying to this email.\n\n"
            f"Best regards,\n"
            f"The Hireloop Hiring Team"
        )

    elif template_type == EmailTemplateType.SELECTED:
        subject = f"Congratulations! You are Selected for {job.title}"

        body = (
            f"Dear {candidate_first_name},\n\n"
            f"Thankyou for your interest in the {job.title} position at our company.\n We are delighted to inform you that you have been SELECTED for the role.\n\n"
            f"Please find the attached offer letter and further instructions.\n\n"
            f"Best regards,\n"
            f"The Hireloop Hiring Team"
        )

    elif template_type == EmailTemplateType.REJECTED:
        subject = f"Application Update- {job.title}"
        body = (
            f"Dear {candidate_first_name},\n\n"
            f"Thankyou for your interest in the {job.title}"
            "After careful consideration, we regret to inform to you that "
            "we will not be moving forward with your application at this time.\n\n"
            "we appriciate the time and effort you invested in our application process.\n\n"
            "and wish you all the best in your future endeavors.\n\n"
            "Best regards,\n"
            "The Hireloop Hiring Team"
        )

    else:
        subject = f"Update on your application-{job.title}"

        body-(
            f"dear -{candidate_first_name},\n\n"
            f"we would like to provide you with an update regarding your application for the {job.title} position at our company.\n\n"
            f"Please note that we are still in the process of reviewing applications and conducting interviews. We appreciate your patience during this time. we will contact you with further updates soon.\n\n"
            f"if you have any questions or require further information, please feel free to reach out to us.\n\n"
            f"Best regards,\n"
            f"The Hireloop Hiring Team"
        )

    if notes:
        body = (
            body+f"\n\nAdditional Notes:\n{notes}"
            + notes
        )

    return {
        "application_id": application.id,
        "job_title": job.title,
        "template_type": template_type,
        "candidate_name": candidate.name,
        "subject": subject,
        "body": body,
    }
