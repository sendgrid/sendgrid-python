from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.reverse_dns.v3.models.reverse_dns_a_record import ReverseDnsARecord
from sendgrid.rest.api.reverse_dns.v3.models.reverse_dns_users_inner import ReverseDnsUsersInner



class ReverseDns:
    def __init__(
            self,
            id: Optional[int]=None,
            ip: Optional[str]=None,
            rdns: Optional[str]=None,
            users: Optional[List[ReverseDnsUsersInner]]=None,
            subdomain: Optional[str]=None,
            domain: Optional[str]=None,
            valid: Optional[bool]=None,
            legacy: Optional[bool]=None,
            last_validation_attempt_at: Optional[int]=None,
            a_record: Optional[ReverseDnsARecord]=None
    ):
        self.id=id
        self.ip=ip
        self.rdns=rdns
        self.users=users
        self.subdomain=subdomain
        self.domain=domain
        self.valid=valid
        self.legacy=legacy
        self.last_validation_attempt_at=last_validation_attempt_at
        self.a_record=a_record

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "id": self.id,
            "ip": self.ip,
            "rdns": self.rdns,
            "users": self.users,
            "subdomain": self.subdomain,
            "domain": self.domain,
            "valid": self.valid,
            "legacy": self.legacy,
            "last_validation_attempt_at": self.last_validation_attempt_at,
            "a_record": self.a_record
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ReverseDns(
            id=payload.get('id'),
            ip=payload.get('ip'),
            rdns=payload.get('rdns'),
            users=payload.get('users'),
            subdomain=payload.get('subdomain'),
            domain=payload.get('domain'),
            valid=payload.get('valid'),
            legacy=payload.get('legacy'),
            last_validation_attempt_at=payload.get('last_validation_attempt_at'),
            a_record=payload.get('a_record')
        ) 

