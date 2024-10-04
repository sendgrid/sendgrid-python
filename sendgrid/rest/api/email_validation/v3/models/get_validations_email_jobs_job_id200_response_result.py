from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.email_validation.v3.models.get_validations_email_jobs_job_id200_response_result_errors_inner import (
    GetValidationsEmailJobsJobId200ResponseResultErrorsInner,
)
from sendgrid.rest.api.email_validation.v3.models.status1 import Status1


class GetValidationsEmailJobsJobId200ResponseResult:
    def __init__(
        self,
        id: Optional[str] = None,
        status: Optional[Status1] = None,
        segments: Optional[float] = None,
        segments_processed: Optional[float] = None,
        is_download_available: Optional[bool] = None,
        started_at: Optional[float] = None,
        finished_at: Optional[float] = None,
        errors: Optional[
            List[GetValidationsEmailJobsJobId200ResponseResultErrorsInner]
        ] = None,
    ):
        self.id = id
        self.status = status
        self.segments = segments
        self.segments_processed = segments_processed
        self.is_download_available = is_download_available
        self.started_at = started_at
        self.finished_at = finished_at
        self.errors = errors

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "status": self.status,
                "segments": self.segments,
                "segments_processed": self.segments_processed,
                "is_download_available": self.is_download_available,
                "started_at": self.started_at,
                "finished_at": self.finished_at,
                "errors": self.errors,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetValidationsEmailJobsJobId200ResponseResult(
            id=payload.get("id"),
            status=payload.get("status"),
            segments=payload.get("segments"),
            segments_processed=payload.get("segments_processed"),
            is_download_available=payload.get("is_download_available"),
            started_at=payload.get("started_at"),
            finished_at=payload.get("finished_at"),
            errors=payload.get("errors"),
        )
