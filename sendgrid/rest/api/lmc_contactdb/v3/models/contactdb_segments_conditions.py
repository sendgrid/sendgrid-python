from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.lmc_contactdb.v3.models.and_or import AndOr
from sendgrid.rest.api.lmc_contactdb.v3.models.operator import Operator



class ContactdbSegmentsConditions:
    def __init__(
            self,
            field: Optional[str]=None,
            value: Optional[str]=None,
            operator: Optional[Operator]=None,
            and_or: Optional[AndOr]=None
    ):
        self.field=field
        self.value=value
        self.operator=operator
        self.and_or=and_or

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "field": self.field,
            "value": self.value,
            "operator": self.operator,
            "and_or": self.and_or
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ContactdbSegmentsConditions(
            field=payload.get('field'),
            value=payload.get('value'),
            operator=payload.get('operator'),
            and_or=payload.get('and_or')
        ) 

