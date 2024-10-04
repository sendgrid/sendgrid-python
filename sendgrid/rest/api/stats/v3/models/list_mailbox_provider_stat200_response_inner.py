from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.stats.v3.models.list_mailbox_provider_stat200_response_inner_stats_inner import ListMailboxProviderStat200ResponseInnerStatsInner



class ListMailboxProviderStat200ResponseInner:
    def __init__(
            self,
            var_date: Optional[str]=None,
            stats: Optional[List[ListMailboxProviderStat200ResponseInnerStatsInner]]=None
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
        return ListMailboxProviderStat200ResponseInner(
            var_date=payload.get('date'),
            stats=payload.get('stats')
        ) 

