from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_contacts.v3.models.import_contact200_response_upload_headers_inner import ImportContact200ResponseUploadHeadersInner



class ImportContact200Response:
    def __init__(
            self,
            job_id: Optional[str]=None,
            upload_uri: Optional[str]=None,
            upload_headers: Optional[List[ImportContact200ResponseUploadHeadersInner]]=None
    ):
        self.job_id=job_id
        self.upload_uri=upload_uri
        self.upload_headers=upload_headers

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "job_id": self.job_id,
            "upload_uri": self.upload_uri,
            "upload_headers": self.upload_headers
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ImportContact200Response(
            job_id=payload.get('job_id'),
            upload_uri=payload.get('upload_uri'),
            upload_headers=payload.get('upload_headers')
        ) 
