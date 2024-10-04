from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class AdvancedStatsClicksOpens:
    def __init__(
        self,
        clicks: Optional[int] = None,
        unique_clicks: Optional[int] = None,
        opens: Optional[int] = None,
        unique_opens: Optional[int] = None,
    ):
        self.clicks = clicks
        self.unique_clicks = unique_clicks
        self.opens = opens
        self.unique_opens = unique_opens

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "clicks": self.clicks,
                "unique_clicks": self.unique_clicks,
                "opens": self.opens,
                "unique_opens": self.unique_opens,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AdvancedStatsClicksOpens(
            clicks=payload.get("clicks"),
            unique_clicks=payload.get("unique_clicks"),
            opens=payload.get("opens"),
            unique_opens=payload.get("unique_opens"),
        )
