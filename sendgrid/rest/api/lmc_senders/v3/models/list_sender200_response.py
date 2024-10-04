from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_senders.v3.models.sender_id import SenderId


class ListSender200Response:
    def __init__(self, result: Optional[List[SenderId]] = None):
        self.result = result

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"result": self.result}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListSender200Response(result=payload.get("result"))
