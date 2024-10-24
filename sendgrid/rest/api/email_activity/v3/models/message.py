from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.email_activity.v3.models.event import Event
from sendgrid.rest.api.email_activity.v3.models.outbound_ip_type import OutboundIpType
from sendgrid.rest.api.email_activity.v3.models.status3 import Status3



class Message:
    def __init__(
            self,
            from_email: Optional[str]=None,
            msg_id: Optional[str]=None,
            subject: Optional[str]=None,
            to_email: Optional[str]=None,
            status: Optional[Status3]=None,
            template_id: Optional[str]=None,
            asm_group_id: Optional[int]=None,
            teammate: Optional[str]=None,
            api_key_id: Optional[str]=None,
            events: Optional[List[Event]]=None,
            originating_ip: Optional[str]=None,
            categories: Optional[List[str]]=None,
            unique_args: Optional[str]=None,
            outbound_ip: Optional[str]=None,
            outbound_ip_type: Optional[OutboundIpType]=None
    ):
        self.from_email=from_email
        self.msg_id=msg_id
        self.subject=subject
        self.to_email=to_email
        self.status=status
        self.template_id=template_id
        self.asm_group_id=asm_group_id
        self.teammate=teammate
        self.api_key_id=api_key_id
        self.events=events
        self.originating_ip=originating_ip
        self.categories=categories
        self.unique_args=unique_args
        self.outbound_ip=outbound_ip
        self.outbound_ip_type=outbound_ip_type

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "from_email": self.from_email,
            "msg_id": self.msg_id,
            "subject": self.subject,
            "to_email": self.to_email,
            "status": self.status,
            "template_id": self.template_id,
            "asm_group_id": self.asm_group_id,
            "teammate": self.teammate,
            "api_key_id": self.api_key_id,
            "events": self.events,
            "originating_ip": self.originating_ip,
            "categories": self.categories,
            "unique_args": self.unique_args,
            "outbound_ip": self.outbound_ip,
            "outbound_ip_type": self.outbound_ip_type
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return Message(
            from_email=payload.get('from_email'),
            msg_id=payload.get('msg_id'),
            subject=payload.get('subject'),
            to_email=payload.get('to_email'),
            status=payload.get('status'),
            template_id=payload.get('template_id'),
            asm_group_id=payload.get('asm_group_id'),
            teammate=payload.get('teammate'),
            api_key_id=payload.get('api_key_id'),
            events=payload.get('events'),
            originating_ip=payload.get('originating_ip'),
            categories=payload.get('categories'),
            unique_args=payload.get('unique_args'),
            outbound_ip=payload.get('outbound_ip'),
            outbound_ip_type=payload.get('outbound_ip_type')
        ) 

