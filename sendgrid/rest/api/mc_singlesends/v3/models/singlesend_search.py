from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_singlesends.v3.models.items import Items


class SinglesendSearch:
    def __init__(
        self,
        name: Optional[str] = None,
        status: Optional[List[Items]] = None,
        categories: Optional[List[str]] = None,
    ):
        self.name = name
        self.status = status
        self.categories = categories

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "status": self.status,
                "categories": self.categories,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendSearch(
            name=payload.get("name"),
            status=payload.get("status"),
            categories=payload.get("categories"),
        )
