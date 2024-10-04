from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.enforced_tls.v3.models.version import Version



class EnforcedTlsRequestResponse:
    def __init__(
            self,
            require_tls: Optional[bool]=None,
            require_valid_cert: Optional[bool]=None,
            version: Optional[Version]=None
    ):
        self.require_tls=require_tls
        self.require_valid_cert=require_valid_cert
        self.version=version

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "require_tls": self.require_tls,
            "require_valid_cert": self.require_valid_cert,
            "version": self.version
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return EnforcedTlsRequestResponse(
            require_tls=payload.get('require_tls'),
            require_valid_cert=payload.get('require_valid_cert'),
            version=payload.get('version')
        ) 

