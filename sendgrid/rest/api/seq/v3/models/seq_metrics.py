from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SeqMetrics:
    def __init__(
            self,
            engagement_recency: Optional[float]=None,
            open_rate: Optional[float]=None,
            bounce_classification: Optional[float]=None,
            bounce_rate: Optional[float]=None,
            spam_rate: Optional[float]=None
    ):
        self.engagement_recency=engagement_recency
        self.open_rate=open_rate
        self.bounce_classification=bounce_classification
        self.bounce_rate=bounce_rate
        self.spam_rate=spam_rate

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "engagement_recency": self.engagement_recency,
            "open_rate": self.open_rate,
            "bounce_classification": self.bounce_classification,
            "bounce_rate": self.bounce_rate,
            "spam_rate": self.spam_rate
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SeqMetrics(
            engagement_recency=payload.get('engagement_recency'),
            open_rate=payload.get('open_rate'),
            bounce_classification=payload.get('bounce_classification'),
            bounce_rate=payload.get('bounce_rate'),
            spam_rate=payload.get('spam_rate')
        ) 

