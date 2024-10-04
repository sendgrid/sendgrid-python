from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListIp200ResponseInner:
    def __init__(
        self,
        ip: Optional[str] = None,
        subusers: Optional[List[str]] = None,
        rdns: Optional[str] = None,
        pools: Optional[List[str]] = None,
        warmup: Optional[bool] = None,
        start_date: Optional[float] = None,
        whitelabeled: Optional[bool] = None,
        assigned_at: Optional[int] = None,
    ):
        self.ip = ip
        self.subusers = subusers
        self.rdns = rdns
        self.pools = pools
        self.warmup = warmup
        self.start_date = start_date
        self.whitelabeled = whitelabeled
        self.assigned_at = assigned_at

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "ip": self.ip,
                "subusers": self.subusers,
                "rdns": self.rdns,
                "pools": self.pools,
                "warmup": self.warmup,
                "start_date": self.start_date,
                "whitelabeled": self.whitelabeled,
                "assigned_at": self.assigned_at,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListIp200ResponseInner(
            ip=payload.get("ip"),
            subusers=payload.get("subusers"),
            rdns=payload.get("rdns"),
            pools=payload.get("pools"),
            warmup=payload.get("warmup"),
            start_date=payload.get("start_date"),
            whitelabeled=payload.get("whitelabeled"),
            assigned_at=payload.get("assigned_at"),
        )
