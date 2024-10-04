from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_senders.v3.models.create_sender_request_from import (
    CreateSenderRequestFrom,
)
from sendgrid.rest.api.mc_senders.v3.models.create_sender_request_reply_to import (
    CreateSenderRequestReplyTo,
)


class Sender:
    def __init__(
        self,
        id: Optional[int] = None,
        nickname: Optional[str] = None,
        var_from: Optional[CreateSenderRequestFrom] = None,
        reply_to: Optional[CreateSenderRequestReplyTo] = None,
        address: Optional[str] = None,
        address_2: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None,
        zip: Optional[str] = None,
        country: Optional[str] = None,
        verified: Optional[bool] = None,
        locked: Optional[bool] = None,
        updated_at: Optional[int] = None,
        created_at: Optional[int] = None,
    ):
        self.id = id
        self.nickname = nickname
        self.var_from = var_from
        self.reply_to = reply_to
        self.address = address
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.zip = zip
        self.country = country
        self.verified = verified
        self.locked = locked
        self.updated_at = updated_at
        self.created_at = created_at

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "id": self.id,
                "nickname": self.nickname,
                "from": self.var_from,
                "reply_to": self.reply_to,
                "address": self.address,
                "address_2": self.address_2,
                "city": self.city,
                "state": self.state,
                "zip": self.zip,
                "country": self.country,
                "verified": self.verified,
                "locked": self.locked,
                "updated_at": self.updated_at,
                "created_at": self.created_at,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Sender(
            id=payload.get("id"),
            nickname=payload.get("nickname"),
            var_from=payload.get("from"),
            reply_to=payload.get("reply_to"),
            address=payload.get("address"),
            address_2=payload.get("address_2"),
            city=payload.get("city"),
            state=payload.get("state"),
            zip=payload.get("zip"),
            country=payload.get("country"),
            verified=payload.get("verified"),
            locked=payload.get("locked"),
            updated_at=payload.get("updated_at"),
            created_at=payload.get("created_at"),
        )
