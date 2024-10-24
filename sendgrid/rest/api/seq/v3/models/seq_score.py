from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.seq.v3.models.seq_metrics import SeqMetrics



class SeqScore:
    def __init__(
            self,
            user_id: Optional[str]=None,
            username: Optional[str]=None,
            var_date: Optional[date]=None,
            score: Optional[float]=None,
            metrics: Optional[SeqMetrics]=None
    ):
        self.user_id=user_id
        self.username=username
        self.var_date=var_date
        self.score=score
        self.metrics=metrics

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "user_id": self.user_id,
            "username": self.username,
            "date": self.var_date,
            "score": self.score,
            "metrics": self.metrics
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SeqScore(
            user_id=payload.get('user_id'),
            username=payload.get('username'),
            var_date=payload.get('date'),
            score=payload.get('score'),
            metrics=payload.get('metrics')
        ) 

