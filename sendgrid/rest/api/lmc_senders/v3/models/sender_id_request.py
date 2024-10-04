from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_senders.v3.models.sender_id_request_from import (
    SenderIdRequestFrom,
)
from sendgrid.rest.api.lmc_senders.v3.models.sender_id_request_reply_to import (
    SenderIdRequestReplyTo,
)


class SenderIdRequest:
    def __init__(
        self,
        nickname: Optional[str] = None,
        var_from: Optional[SenderIdRequestFrom] = None,
        reply_to: Optional[SenderIdRequestReplyTo] = None,
        address: Optional[str] = None,
        address_2: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        country: Optional[str] = None,
    ):
        self.nickname = nickname
        self.var_from = var_from
        self.reply_to = reply_to
        self.address = address
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "nickname": self.nickname,
                "from": self.var_from,
                "reply_to": self.reply_to,
                "address": self.address,
                "address_2": self.address_2,
                "city": self.city,
                "state": self.state,
                "zip": self.zip,
                "country": self.country,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SenderIdRequest(
            nickname=payload.get("nickname"),
            var_from=payload.get("from"),
            reply_to=payload.get("reply_to"),
            address=payload.get("address"),
            address_2=payload.get("address_2"),
            city=payload.get("city"),
            state=payload.get("state"),
            zip=payload.get("zip"),
            country=payload.get("country"),
        )
