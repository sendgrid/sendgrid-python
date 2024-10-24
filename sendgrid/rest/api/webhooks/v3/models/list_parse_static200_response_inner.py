from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.webhooks.v3.models.list_parse_static200_response_inner_stats_inner import ListParseStatic200ResponseInnerStatsInner



class ListParseStatic200ResponseInner:
    def __init__(
            self,
            var_date: Optional[str]=None,
            stats: Optional[List[ListParseStatic200ResponseInnerStatsInner]]=None
    ):
        self.var_date=var_date
        self.stats=stats

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "date": self.var_date,
            "stats": self.stats
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListParseStatic200ResponseInner(
            var_date=payload.get('date'),
            stats=payload.get('stats')
        ) 

