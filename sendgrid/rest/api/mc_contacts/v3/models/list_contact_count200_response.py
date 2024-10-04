from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.list_contact_count200_response_billable_breakdown import ListContactCount200ResponseBillableBreakdown



class ListContactCount200Response:
    def __init__(
            self,
            contact_count: Optional[int]=None,
            billable_count: Optional[int]=None,
            billable_breakdown: Optional[ListContactCount200ResponseBillableBreakdown]=None
    ):
        self.contact_count=contact_count
        self.billable_count=billable_count
        self.billable_breakdown=billable_breakdown

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "contact_count": self.contact_count,
            "billable_count": self.billable_count,
            "billable_breakdown": self.billable_breakdown
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListContactCount200Response(
            contact_count=payload.get('contact_count'),
            billable_count=payload.get('billable_count'),
            billable_breakdown=payload.get('billable_breakdown')
        ) 

