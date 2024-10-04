from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mail.v3.models.mail_from import MailFrom
from sendgrid.rest.api.mail.v3.models.mail_to import MailTo


class SendMailRequestPersonalizationsInner:
    def __init__(
        self,
        var_from: Optional[MailFrom] = None,
        to: Optional[List[MailTo]] = None,
        cc: Optional[List[MailTo]] = None,
        bcc: Optional[List[MailTo]] = None,
        subject: Optional[str] = None,
        headers: Optional[object] = None,
        substitutions: Optional[Dict[str, str]] = None,
        dynamic_template_data: Optional[object] = None,
        custom_args: Optional[object] = None,
        send_at: Optional[int] = None,
    ):
        self.var_from = var_from
        self.to = to
        self.cc = cc
        self.bcc = bcc
        self.subject = subject
        self.headers = headers
        self.substitutions = substitutions
        self.dynamic_template_data = dynamic_template_data
        self.custom_args = custom_args
        self.send_at = send_at

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "from": self.var_from,
                "to": self.to,
                "cc": self.cc,
                "bcc": self.bcc,
                "subject": self.subject,
                "headers": self.headers,
                "substitutions": self.substitutions,
                "dynamic_template_data": self.dynamic_template_data,
                "custom_args": self.custom_args,
                "send_at": self.send_at,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestPersonalizationsInner(
            var_from=payload.get("from"),
            to=payload.get("to"),
            cc=payload.get("cc"),
            bcc=payload.get("bcc"),
            subject=payload.get("subject"),
            headers=payload.get("headers"),
            substitutions=payload.get("substitutions"),
            dynamic_template_data=payload.get("dynamic_template_data"),
            custom_args=payload.get("custom_args"),
            send_at=payload.get("send_at"),
        )
