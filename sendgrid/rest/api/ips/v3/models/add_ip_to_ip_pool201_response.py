from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class AddIpToIpPool201Response:
    def __init__(
        self,
        ip: Optional[str] = None,
        pools: Optional[List[str]] = None,
        start_date: Optional[int] = None,
        warmup: Optional[bool] = None,
    ):
        self.ip = ip
        self.pools = pools
        self.start_date = start_date
        self.warmup = warmup

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "ip": self.ip,
                "pools": self.pools,
                "start_date": self.start_date,
                "warmup": self.warmup,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIpToIpPool201Response(
            ip=payload.get("ip"),
            pools=payload.get("pools"),
            start_date=payload.get("start_date"),
            warmup=payload.get("warmup"),
        )
