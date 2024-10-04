from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListAssignedIp200ResponseInner:
    def __init__(
        self,
        ip: Optional[str] = None,
        pools: Optional[List[str]] = None,
        warmup: Optional[bool] = None,
        start_date: Optional[int] = None,
    ):
        self.ip = ip
        self.pools = pools
        self.warmup = warmup
        self.start_date = start_date

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "ip": self.ip,
                "pools": self.pools,
                "warmup": self.warmup,
                "start_date": self.start_date,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListAssignedIp200ResponseInner(
            ip=payload.get("ip"),
            pools=payload.get("pools"),
            warmup=payload.get("warmup"),
            start_date=payload.get("start_date"),
        )
