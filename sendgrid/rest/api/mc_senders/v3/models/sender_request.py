from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mc_senders.v3.models.sender_request_from import SenderRequestFrom
from sendgrid.rest.api.mc_senders.v3.models.sender_request_reply_to import SenderRequestReplyTo



class SenderRequest:
    def __init__(
            self,
            nickname: Optional[str]=None,
            var_from: Optional[SenderRequestFrom]=None,
            reply_to: Optional[SenderRequestReplyTo]=None,
            address: Optional[str]=None,
            address_2: Optional[str]=None,
            city: Optional[str]=None,
            state: Optional[str]=None,
            zip: Optional[str]=None,
            country: Optional[str]=None
    ):
        self.nickname=nickname
        self.var_from=var_from
        self.reply_to=reply_to
        self.address=address
        self.address_2=address_2
        self.city=city
        self.state=state
        self.zip=zip
        self.country=country

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "nickname": self.nickname,
            "from": self.var_from,
            "reply_to": self.reply_to,
            "address": self.address,
            "address_2": self.address_2,
            "city": self.city,
            "state": self.state,
            "zip": self.zip,
            "country": self.country
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SenderRequest(
            nickname=payload.get('nickname'),
            var_from=payload.get('from'),
            reply_to=payload.get('reply_to'),
            address=payload.get('address'),
            address_2=payload.get('address_2'),
            city=payload.get('city'),
            state=payload.get('state'),
            zip=payload.get('zip'),
            country=payload.get('country')
        ) 

