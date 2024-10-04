from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class DeleteContact202Response:
    def __init__(self, job_id: Optional[object] = None):
        self.job_id = job_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"job_id": self.job_id}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DeleteContact202Response(job_id=payload.get("job_id"))
