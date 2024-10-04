from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class Metrics:
    def __init__(
        self,
        bounce_drops: Optional[int] = None,
        bounces: Optional[int] = None,
        clicks: Optional[int] = None,
        delivered: Optional[int] = None,
        invalid_emails: Optional[int] = None,
        opens: Optional[int] = None,
        requests: Optional[int] = None,
        spam_report_drops: Optional[int] = None,
        spam_reports: Optional[int] = None,
        unique_clicks: Optional[int] = None,
        unique_opens: Optional[int] = None,
        unsubscribes: Optional[int] = None,
    ):
        self.bounce_drops = bounce_drops
        self.bounces = bounces
        self.clicks = clicks
        self.delivered = delivered
        self.invalid_emails = invalid_emails
        self.opens = opens
        self.requests = requests
        self.spam_report_drops = spam_report_drops
        self.spam_reports = spam_reports
        self.unique_clicks = unique_clicks
        self.unique_opens = unique_opens
        self.unsubscribes = unsubscribes

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "bounce_drops": self.bounce_drops,
                "bounces": self.bounces,
                "clicks": self.clicks,
                "delivered": self.delivered,
                "invalid_emails": self.invalid_emails,
                "opens": self.opens,
                "requests": self.requests,
                "spam_report_drops": self.spam_report_drops,
                "spam_reports": self.spam_reports,
                "unique_clicks": self.unique_clicks,
                "unique_opens": self.unique_opens,
                "unsubscribes": self.unsubscribes,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Metrics(
            bounce_drops=payload.get("bounce_drops"),
            bounces=payload.get("bounces"),
            clicks=payload.get("clicks"),
            delivered=payload.get("delivered"),
            invalid_emails=payload.get("invalid_emails"),
            opens=payload.get("opens"),
            requests=payload.get("requests"),
            spam_report_drops=payload.get("spam_report_drops"),
            spam_reports=payload.get("spam_reports"),
            unique_clicks=payload.get("unique_clicks"),
            unique_opens=payload.get("unique_opens"),
            unsubscribes=payload.get("unsubscribes"),
        )
