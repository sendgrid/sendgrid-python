from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_contacts.v3.models.contact_import_results import (
    ContactImportResults,
)


class ContactImport:
    def __init__(
        self,
        id: Optional[str] = None,
        status: Optional[str] = None,
        job_type: Optional[str] = None,
        results: Optional[ContactImportResults] = None,
        started_at: Optional[str] = None,
        finished_at: Optional[str] = None,
    ):
        self.id = id
        self.status = status
        self.job_type = job_type
        self.results = results
        self.started_at = started_at
        self.finished_at = finished_at

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "status": self.status,
                "job_type": self.job_type,
                "results": self.results,
                "started_at": self.started_at,
                "finished_at": self.finished_at,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactImport(
            id=payload.get("id"),
            status=payload.get("status"),
            job_type=payload.get("job_type"),
            results=payload.get("results"),
            started_at=payload.get("started_at"),
            finished_at=payload.get("finished_at"),
        )
