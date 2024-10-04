from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.lmc_senders.v3.models.sender_id_request_from import (
    SenderIdRequestFrom,
)
from sendgrid.rest.api.lmc_senders.v3.models.sender_id_request_reply_to import (
    SenderIdRequestReplyTo,
)


class SenderId:
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
        id: Optional[int] = None,
        verified: Optional[bool] = None,
        updated_at: Optional[int] = None,
        created_at: Optional[int] = None,
        locked: Optional[bool] = None,
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
        self.id = id
        self.verified = verified
        self.updated_at = updated_at
        self.created_at = created_at
        self.locked = locked

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
                "id": self.id,
                "verified": self.verified,
                "updated_at": self.updated_at,
                "created_at": self.created_at,
                "locked": self.locked,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SenderId(
            nickname=payload.get("nickname"),
            var_from=payload.get("from"),
            reply_to=payload.get("reply_to"),
            address=payload.get("address"),
            address_2=payload.get("address_2"),
            city=payload.get("city"),
            state=payload.get("state"),
            zip=payload.get("zip"),
            country=payload.get("country"),
            id=payload.get("id"),
            verified=payload.get("verified"),
            updated_at=payload.get("updated_at"),
            created_at=payload.get("created_at"),
            locked=payload.get("locked"),
        )
