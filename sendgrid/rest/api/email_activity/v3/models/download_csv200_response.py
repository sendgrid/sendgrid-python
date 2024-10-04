from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class DownloadCsv200Response:
    def __init__(
            self,
            presigned_url: Optional[str]=None,
            csv: Optional[str]=None
    ):
        self.presigned_url=presigned_url
        self.csv=csv

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "presigned_url": self.presigned_url,
            "csv": self.csv
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return DownloadCsv200Response(
            presigned_url=payload.get('presigned_url'),
            csv=payload.get('csv')
        ) 

