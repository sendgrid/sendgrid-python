from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class VerifiedSenderRequest:
    def __init__(
        self,
        nickname: Optional[str] = None,
        from_email: Optional[str] = None,
        from_name: Optional[str] = None,
        reply_to: Optional[str] = None,
        reply_to_name: Optional[str] = None,
        address: Optional[str] = None,
        address2: Optional[str] = None,
        state: Optional[str] = None,
        city: Optional[str] = None,
        zip: Optional[str] = None,
        country: Optional[str] = None,
    ):
        self.nickname = nickname
        self.from_email = from_email
        self.from_name = from_name
        self.reply_to = reply_to
        self.reply_to_name = reply_to_name
        self.address = address
        self.address2 = address2
        self.state = state
        self.city = city
        self.zip = zip
        self.country = country

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "nickname": self.nickname,
                "from_email": self.from_email,
                "from_name": self.from_name,
                "reply_to": self.reply_to,
                "reply_to_name": self.reply_to_name,
                "address": self.address,
                "address2": self.address2,
                "state": self.state,
                "city": self.city,
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
        return VerifiedSenderRequest(
            nickname=payload.get("nickname"),
            from_email=payload.get("from_email"),
            from_name=payload.get("from_name"),
            reply_to=payload.get("reply_to"),
            reply_to_name=payload.get("reply_to_name"),
            address=payload.get("address"),
            address2=payload.get("address2"),
            state=payload.get("state"),
            city=payload.get("city"),
            zip=payload.get("zip"),
            country=payload.get("country"),
        )
