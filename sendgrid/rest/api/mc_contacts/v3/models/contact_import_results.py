from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class ContactImportResults:
    def __init__(
            self,
            requested_count: Optional[float]=None,
            created_count: Optional[float]=None,
            updated_count: Optional[float]=None,
            deleted_count: Optional[float]=None,
            errored_count: Optional[float]=None,
            errors_url: Optional[str]=None
    ):
        self.requested_count=requested_count
        self.created_count=created_count
        self.updated_count=updated_count
        self.deleted_count=deleted_count
        self.errored_count=errored_count
        self.errors_url=errors_url

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "requested_count": self.requested_count,
            "created_count": self.created_count,
            "updated_count": self.updated_count,
            "deleted_count": self.deleted_count,
            "errored_count": self.errored_count,
            "errors_url": self.errors_url
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactImportResults(
            requested_count=payload.get('requested_count'),
            created_count=payload.get('created_count'),
            updated_count=payload.get('updated_count'),
            deleted_count=payload.get('deleted_count'),
            errored_count=payload.get('errored_count'),
            errors_url=payload.get('errors_url')
        ) 

