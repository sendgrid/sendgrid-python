from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class GETUserProfileResponse:
    def __init__(
        self,
        address: Optional[str] = None,
        address2: Optional[str] = None,
        city: Optional[str] = None,
        company: Optional[str] = None,
        country: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        phone: Optional[str] = None,
        state: Optional[str] = None,
        website: Optional[str] = None,
        zip: Optional[str] = None,
    ):
        self.address = address
        self.address2 = address2
        self.city = city
        self.company = company
        self.country = country
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.state = state
        self.website = website
        self.zip = zip

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "address": self.address,
                "address2": self.address2,
                "city": self.city,
                "company": self.company,
                "country": self.country,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "phone": self.phone,
                "state": self.state,
                "website": self.website,
                "zip": self.zip,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return GETUserProfileResponse(
            address=payload.get("address"),
            address2=payload.get("address2"),
            city=payload.get("city"),
            company=payload.get("company"),
            country=payload.get("country"),
            first_name=payload.get("first_name"),
            last_name=payload.get("last_name"),
            phone=payload.get("phone"),
            state=payload.get("state"),
            website=payload.get("website"),
            zip=payload.get("zip"),
        )
