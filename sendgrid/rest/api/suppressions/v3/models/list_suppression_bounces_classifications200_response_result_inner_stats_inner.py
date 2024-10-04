from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.suppressions.v3.models.classification import Classification


class ListSuppressionBouncesClassifications200ResponseResultInnerStatsInner:
    def __init__(
        self,
        classification: Optional[Classification] = None,
        count: Optional[int] = None,
    ):
        self.classification = classification
        self.count = count

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "classification": self.classification,
                "count": self.count,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListSuppressionBouncesClassifications200ResponseResultInnerStatsInner(
            classification=payload.get("classification"), count=payload.get("count")
        )
