from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class UpdateSubuserRemainingCreditRequest:
    def __init__(self, allocation_update: Optional[int] = None):
        self.allocation_update = allocation_update

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"allocation_update": self.allocation_update}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return UpdateSubuserRemainingCreditRequest(
            allocation_update=payload.get("allocation_update")
        )
