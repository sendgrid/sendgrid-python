from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class StatsAdvancedGlobalStats:
    def __init__(
        self,
        clicks: Optional[int] = None,
        unique_clicks: Optional[int] = None,
        opens: Optional[int] = None,
        unique_opens: Optional[int] = None,
        blocks: Optional[int] = None,
        bounce_drops: Optional[int] = None,
        bounces: Optional[int] = None,
        deferred: Optional[int] = None,
        delivered: Optional[int] = None,
        invalid_emails: Optional[int] = None,
        processed: Optional[int] = None,
        requests: Optional[int] = None,
        spam_report_drops: Optional[int] = None,
        spam_reports: Optional[int] = None,
        unsubscribe_drops: Optional[int] = None,
        unsubscribes: Optional[int] = None,
    ):
        self.clicks = clicks
        self.unique_clicks = unique_clicks
        self.opens = opens
        self.unique_opens = unique_opens
        self.blocks = blocks
        self.bounce_drops = bounce_drops
        self.bounces = bounces
        self.deferred = deferred
        self.delivered = delivered
        self.invalid_emails = invalid_emails
        self.processed = processed
        self.requests = requests
        self.spam_report_drops = spam_report_drops
        self.spam_reports = spam_reports
        self.unsubscribe_drops = unsubscribe_drops
        self.unsubscribes = unsubscribes

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "clicks": self.clicks,
                "unique_clicks": self.unique_clicks,
                "opens": self.opens,
                "unique_opens": self.unique_opens,
                "blocks": self.blocks,
                "bounce_drops": self.bounce_drops,
                "bounces": self.bounces,
                "deferred": self.deferred,
                "delivered": self.delivered,
                "invalid_emails": self.invalid_emails,
                "processed": self.processed,
                "requests": self.requests,
                "spam_report_drops": self.spam_report_drops,
                "spam_reports": self.spam_reports,
                "unsubscribe_drops": self.unsubscribe_drops,
                "unsubscribes": self.unsubscribes,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return StatsAdvancedGlobalStats(
            clicks=payload.get("clicks"),
            unique_clicks=payload.get("unique_clicks"),
            opens=payload.get("opens"),
            unique_opens=payload.get("unique_opens"),
            blocks=payload.get("blocks"),
            bounce_drops=payload.get("bounce_drops"),
            bounces=payload.get("bounces"),
            deferred=payload.get("deferred"),
            delivered=payload.get("delivered"),
            invalid_emails=payload.get("invalid_emails"),
            processed=payload.get("processed"),
            requests=payload.get("requests"),
            spam_report_drops=payload.get("spam_report_drops"),
            spam_reports=payload.get("spam_reports"),
            unsubscribe_drops=payload.get("unsubscribe_drops"),
            unsubscribes=payload.get("unsubscribes"),
        )
