from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.subusers.v3.models.region1 import Region1


class CreateSubuserRequest:
    def __init__(
        self,
        username: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        ips: Optional[List[str]] = None,
        region: Optional[Region1] = None,
        include_region: Optional[bool] = None,
    ):
        self.username = username
        self.email = email
        self.password = password
        self.ips = ips
        self.region = region
        self.include_region = include_region

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "username": self.username,
                "email": self.email,
                "password": self.password,
                "ips": self.ips,
                "region": self.region,
                "include_region": self.include_region,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CreateSubuserRequest(
            username=payload.get("username"),
            email=payload.get("email"),
            password=payload.get("password"),
            ips=payload.get("ips"),
            region=payload.get("region"),
            include_region=payload.get("include_region"),
        )
