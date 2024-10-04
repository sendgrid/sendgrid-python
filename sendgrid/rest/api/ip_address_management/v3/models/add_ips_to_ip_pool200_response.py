from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class AddIpsToIpPool200Response:
    def __init__(
        self,
        name: Optional[str] = None,
        id: Optional[str] = None,
        ips: Optional[List[str]] = None,
    ):
        self.name = name
        self.id = id
        self.ips = ips

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "name": self.name,
                "id": self.id,
                "ips": self.ips,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIpsToIpPool200Response(
            name=payload.get("name"), id=payload.get("id"), ips=payload.get("ips")
        )
