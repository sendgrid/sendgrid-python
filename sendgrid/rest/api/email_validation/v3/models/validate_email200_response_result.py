from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.email_validation.v3.models.validate_email200_response_result_checks import ValidateEmail200ResponseResultChecks
from sendgrid.rest.api.email_validation.v3.models.verdict import Verdict



class ValidateEmail200ResponseResult:
    def __init__(
            self,
            email: Optional[str]=None,
            verdict: Optional[Verdict]=None,
            score: Optional[float]=None,
            local: Optional[str]=None,
            host: Optional[str]=None,
            suggestion: Optional[str]=None,
            checks: Optional[ValidateEmail200ResponseResultChecks]=None,
            source: Optional[str]=None,
            ip_address: Optional[str]=None
    ):
        self.email=email
        self.verdict=verdict
        self.score=score
        self.local=local
        self.host=host
        self.suggestion=suggestion
        self.checks=checks
        self.source=source
        self.ip_address=ip_address

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "email": self.email,
            "verdict": self.verdict,
            "score": self.score,
            "local": self.local,
            "host": self.host,
            "suggestion": self.suggestion,
            "checks": self.checks,
            "source": self.source,
            "ip_address": self.ip_address
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateEmail200ResponseResult(
            email=payload.get('email'),
            verdict=payload.get('verdict'),
            score=payload.get('score'),
            local=payload.get('local'),
            host=payload.get('host'),
            suggestion=payload.get('suggestion'),
            checks=payload.get('checks'),
            source=payload.get('source'),
            ip_address=payload.get('ip_address')
        ) 

