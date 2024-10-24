from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.mail.v3.models.send_mail_request_mail_settings_bypass_bounce_management import SendMailRequestMailSettingsBypassBounceManagement
from sendgrid.rest.api.mail.v3.models.send_mail_request_mail_settings_bypass_list_management import SendMailRequestMailSettingsBypassListManagement
from sendgrid.rest.api.mail.v3.models.send_mail_request_mail_settings_bypass_spam_management import SendMailRequestMailSettingsBypassSpamManagement
from sendgrid.rest.api.mail.v3.models.send_mail_request_mail_settings_bypass_unsubscribe_management import SendMailRequestMailSettingsBypassUnsubscribeManagement
from sendgrid.rest.api.mail.v3.models.send_mail_request_mail_settings_footer import SendMailRequestMailSettingsFooter
from sendgrid.rest.api.mail.v3.models.send_mail_request_mail_settings_sandbox_mode import SendMailRequestMailSettingsSandboxMode



class SendMailRequestMailSettings:
    def __init__(
            self,
            bypass_list_management: Optional[SendMailRequestMailSettingsBypassListManagement]=None,
            bypass_spam_management: Optional[SendMailRequestMailSettingsBypassSpamManagement]=None,
            bypass_bounce_management: Optional[SendMailRequestMailSettingsBypassBounceManagement]=None,
            bypass_unsubscribe_management: Optional[SendMailRequestMailSettingsBypassUnsubscribeManagement]=None,
            footer: Optional[SendMailRequestMailSettingsFooter]=None,
            sandbox_mode: Optional[SendMailRequestMailSettingsSandboxMode]=None
    ):
        self.bypass_list_management=bypass_list_management
        self.bypass_spam_management=bypass_spam_management
        self.bypass_bounce_management=bypass_bounce_management
        self.bypass_unsubscribe_management=bypass_unsubscribe_management
        self.footer=footer
        self.sandbox_mode=sandbox_mode

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "bypass_list_management": self.bypass_list_management,
            "bypass_spam_management": self.bypass_spam_management,
            "bypass_bounce_management": self.bypass_bounce_management,
            "bypass_unsubscribe_management": self.bypass_unsubscribe_management,
            "footer": self.footer,
            "sandbox_mode": self.sandbox_mode
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return SendMailRequestMailSettings(
            bypass_list_management=payload.get('bypass_list_management'),
            bypass_spam_management=payload.get('bypass_spam_management'),
            bypass_bounce_management=payload.get('bypass_bounce_management'),
            bypass_unsubscribe_management=payload.get('bypass_unsubscribe_management'),
            footer=payload.get('footer'),
            sandbox_mode=payload.get('sandbox_mode')
        ) 

