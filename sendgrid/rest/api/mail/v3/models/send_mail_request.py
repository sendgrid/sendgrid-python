from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mail.v3.models.mail_from import MailFrom
from sendgrid.rest.api.mail.v3.models.mail_to import MailTo
from sendgrid.rest.api.mail.v3.models.send_mail_request_asm import SendMailRequestAsm
from sendgrid.rest.api.mail.v3.models.send_mail_request_attachments_inner import (
    SendMailRequestAttachmentsInner,
)
from sendgrid.rest.api.mail.v3.models.send_mail_request_content_inner import (
    SendMailRequestContentInner,
)
from sendgrid.rest.api.mail.v3.models.send_mail_request_mail_settings import (
    SendMailRequestMailSettings,
)
from sendgrid.rest.api.mail.v3.models.send_mail_request_personalizations_inner import (
    SendMailRequestPersonalizationsInner,
)
from sendgrid.rest.api.mail.v3.models.send_mail_request_tracking_settings import (
    SendMailRequestTrackingSettings,
)


class SendMailRequest:
    def __init__(
        self,
        personalizations: Optional[List[SendMailRequestPersonalizationsInner]] = None,
        var_from: Optional[MailFrom] = None,
        reply_to: Optional[MailTo] = None,
        reply_to_list: Optional[List[MailTo]] = None,
        subject: Optional[str] = None,
        content: Optional[List[SendMailRequestContentInner]] = None,
        attachments: Optional[List[SendMailRequestAttachmentsInner]] = None,
        template_id: Optional[str] = None,
        headers: Optional[object] = None,
        categories: Optional[List[str]] = None,
        custom_args: Optional[str] = None,
        send_at: Optional[int] = None,
        batch_id: Optional[str] = None,
        asm: Optional[SendMailRequestAsm] = None,
        ip_pool_name: Optional[str] = None,
        mail_settings: Optional[SendMailRequestMailSettings] = None,
        tracking_settings: Optional[SendMailRequestTrackingSettings] = None,
    ):
        self.personalizations = personalizations
        self.var_from = var_from
        self.reply_to = reply_to
        self.reply_to_list = reply_to_list
        self.subject = subject
        self.content = content
        self.attachments = attachments
        self.template_id = template_id
        self.headers = headers
        self.categories = categories
        self.custom_args = custom_args
        self.send_at = send_at
        self.batch_id = batch_id
        self.asm = asm
        self.ip_pool_name = ip_pool_name
        self.mail_settings = mail_settings
        self.tracking_settings = tracking_settings

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "personalizations": self.personalizations,
                "from": self.var_from,
                "reply_to": self.reply_to,
                "reply_to_list": self.reply_to_list,
                "subject": self.subject,
                "content": self.content,
                "attachments": self.attachments,
                "template_id": self.template_id,
                "headers": self.headers,
                "categories": self.categories,
                "custom_args": self.custom_args,
                "send_at": self.send_at,
                "batch_id": self.batch_id,
                "asm": self.asm,
                "ip_pool_name": self.ip_pool_name,
                "mail_settings": self.mail_settings,
                "tracking_settings": self.tracking_settings,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequest(
            personalizations=payload.get("personalizations"),
            var_from=payload.get("from"),
            reply_to=payload.get("reply_to"),
            reply_to_list=payload.get("reply_to_list"),
            subject=payload.get("subject"),
            content=payload.get("content"),
            attachments=payload.get("attachments"),
            template_id=payload.get("template_id"),
            headers=payload.get("headers"),
            categories=payload.get("categories"),
            custom_args=payload.get("custom_args"),
            send_at=payload.get("send_at"),
            batch_id=payload.get("batch_id"),
            asm=payload.get("asm"),
            ip_pool_name=payload.get("ip_pool_name"),
            mail_settings=payload.get("mail_settings"),
            tracking_settings=payload.get("tracking_settings"),
        )
