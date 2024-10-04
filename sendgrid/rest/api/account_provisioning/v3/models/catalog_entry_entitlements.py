from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class CatalogEntryEntitlements:
    def __init__(
            self,
            email_sends_max_monthly: Optional[int]=None,
            ip_count: Optional[int]=None,
            teammates_max_total: Optional[int]=None,
            users_max_total: Optional[int]=None
    ):
        self.email_sends_max_monthly=email_sends_max_monthly
        self.ip_count=ip_count
        self.teammates_max_total=teammates_max_total
        self.users_max_total=users_max_total

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "email_sends_max_monthly": self.email_sends_max_monthly,
            "ip_count": self.ip_count,
            "teammates_max_total": self.teammates_max_total,
            "users_max_total": self.users_max_total
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CatalogEntryEntitlements(
            email_sends_max_monthly=payload.get('email_sends_max_monthly'),
            ip_count=payload.get('ip_count'),
            teammates_max_total=payload.get('teammates_max_total'),
            users_max_total=payload.get('users_max_total')
        ) 

