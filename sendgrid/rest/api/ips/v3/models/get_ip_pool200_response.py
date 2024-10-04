from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class GetIpPool200Response:
    def __init__(
        self, pool_name: Optional[str] = None, ips: Optional[List[str]] = None
    ):
        self.pool_name = pool_name
        self.ips = ips

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"pool_name": self.pool_name, "ips": self.ips}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GetIpPool200Response(
            pool_name=payload.get("pool_name"), ips=payload.get("ips")
        )
