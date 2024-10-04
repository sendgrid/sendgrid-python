from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AdvancedStatsMailboxProvider:
    def __init__(
        self,
        blocks: Optional[int] = None,
        bounces: Optional[int] = None,
        deferred: Optional[int] = None,
        delivered: Optional[int] = None,
        drops: Optional[int] = None,
        requests: Optional[int] = None,
        processed: Optional[int] = None,
        spam_reports: Optional[int] = None,
    ):
        self.blocks = blocks
        self.bounces = bounces
        self.deferred = deferred
        self.delivered = delivered
        self.drops = drops
        self.requests = requests
        self.processed = processed
        self.spam_reports = spam_reports

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "blocks": self.blocks,
                "bounces": self.bounces,
                "deferred": self.deferred,
                "delivered": self.delivered,
                "drops": self.drops,
                "requests": self.requests,
                "processed": self.processed,
                "spam_reports": self.spam_reports,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AdvancedStatsMailboxProvider(
            blocks=payload.get("blocks"),
            bounces=payload.get("bounces"),
            deferred=payload.get("deferred"),
            delivered=payload.get("delivered"),
            drops=payload.get("drops"),
            requests=payload.get("requests"),
            processed=payload.get("processed"),
            spam_reports=payload.get("spam_reports"),
        )
