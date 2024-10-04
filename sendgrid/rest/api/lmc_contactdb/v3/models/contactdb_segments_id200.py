from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_contactdb.v3.models.contactdb_segments_conditions import (
    ContactdbSegmentsConditions,
)


class ContactdbSegmentsId200:
    def __init__(
        self,
        id: Optional[float] = None,
        name: Optional[str] = None,
        list_id: Optional[int] = None,
        conditions: Optional[List[ContactdbSegmentsConditions]] = None,
        recipient_count: Optional[float] = None,
    ):
        self.id = id
        self.name = name
        self.list_id = list_id
        self.conditions = conditions
        self.recipient_count = recipient_count

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "name": self.name,
                "list_id": self.list_id,
                "conditions": self.conditions,
                "recipient_count": self.recipient_count,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactdbSegmentsId200(
            id=payload.get("id"),
            name=payload.get("name"),
            list_id=payload.get("list_id"),
            conditions=payload.get("conditions"),
            recipient_count=payload.get("recipient_count"),
        )
