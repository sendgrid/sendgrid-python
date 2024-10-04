from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_stats.v3.models.ab_phase1 import AbPhase1


class SinglesendsLinkStatsResponseResultsInner:
    def __init__(
        self,
        url: Optional[str] = None,
        url_location: Optional[int] = None,
        ab_variation: Optional[str] = None,
        ab_phase: Optional[AbPhase1] = None,
        clicks: Optional[int] = None,
    ):
        self.url = url
        self.url_location = url_location
        self.ab_variation = ab_variation
        self.ab_phase = ab_phase
        self.clicks = clicks

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "url": self.url,
                "url_location": self.url_location,
                "ab_variation": self.ab_variation,
                "ab_phase": self.ab_phase,
                "clicks": self.clicks,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SinglesendsLinkStatsResponseResultsInner(
            url=payload.get("url"),
            url_location=payload.get("url_location"),
            ab_variation=payload.get("ab_variation"),
            ab_phase=payload.get("ab_phase"),
            clicks=payload.get("clicks"),
        )
