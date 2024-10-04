"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Suppressions API
  The Twilio SendGrid Suppressions API allows you to manage your Suppressions or Unsubscribes and Suppression or Unsubscribe groups. With SendGrid, an unsubscribe is the action an email recipient takes when they opt-out of receiving your messages. A suppression is the action you take as a sender to filter or suppress an unsubscribed address from your email send. From the perspective of the recipient, your suppression is the result of their unsubscribe.  You can have global suppressions, which represent addresses that have been unsubscribed from all of your emails. You can also have suppression groups, also known as ASM groups, which represent categories or groups of emails that your recipients can unsubscribe from, rather than unsubscribing from all of your messages.  SendGrid automatically suppresses emails sent to users for a variety of reasons, including blocks, bounces, invalid email addresses, spam reports, and unsubscribes. SendGrid suppresses these messages to help you maintain the best possible sender reputation by attempting to prevent unwanted mail. You may also add addresses to your suppressions.  See [**Suppressions**](https://docs.sendgrid.com/for-developers/sending-email/suppressions) for more information.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

# import models into model package
from sendgrid.rest.api.suppressions.v3.models.accept import Accept
from sendgrid.rest.api.suppressions.v3.models.accept1 import Accept1
from sendgrid.rest.api.suppressions.v3.models.add_suppression_to_asm_group201_response import (
    AddSuppressionToAsmGroup201Response,
)
from sendgrid.rest.api.suppressions.v3.models.blocks_response_inner import (
    BlocksResponseInner,
)
from sendgrid.rest.api.suppressions.v3.models.bounce_response import BounceResponse
from sendgrid.rest.api.suppressions.v3.models.classification import Classification
from sendgrid.rest.api.suppressions.v3.models.classification1 import Classification1
from sendgrid.rest.api.suppressions.v3.models.creat_asm_group201_response import (
    CreatAsmGroup201Response,
)
from sendgrid.rest.api.suppressions.v3.models.create_global_suppression201_response import (
    CreateGlobalSuppression201Response,
)
from sendgrid.rest.api.suppressions.v3.models.delete_invalid_emails_request import (
    DeleteInvalidEmailsRequest,
)
from sendgrid.rest.api.suppressions.v3.models.delete_spam_reports_request import (
    DeleteSpamReportsRequest,
)
from sendgrid.rest.api.suppressions.v3.models.delete_suppression_blocks_request import (
    DeleteSuppressionBlocksRequest,
)
from sendgrid.rest.api.suppressions.v3.models.delete_suppression_bounces_request import (
    DeleteSuppressionBouncesRequest,
)
from sendgrid.rest.api.suppressions.v3.models.error_response import ErrorResponse
from sendgrid.rest.api.suppressions.v3.models.error_response_errors_inner import (
    ErrorResponseErrorsInner,
)
from sendgrid.rest.api.suppressions.v3.models.get_asm_group200_response import (
    GetAsmGroup200Response,
)
from sendgrid.rest.api.suppressions.v3.models.get_asm_suppression200_response import (
    GetAsmSuppression200Response,
)
from sendgrid.rest.api.suppressions.v3.models.get_asm_suppression200_response_suppressions_inner import (
    GetAsmSuppression200ResponseSuppressionsInner,
)
from sendgrid.rest.api.suppressions.v3.models.get_suppression_bounces_classifications200_response import (
    GetSuppressionBouncesClassifications200Response,
)
from sendgrid.rest.api.suppressions.v3.models.get_suppression_bounces_classifications200_response_result_inner import (
    GetSuppressionBouncesClassifications200ResponseResultInner,
)
from sendgrid.rest.api.suppressions.v3.models.get_suppression_bounces_classifications200_response_result_inner_stats_inner import (
    GetSuppressionBouncesClassifications200ResponseResultInnerStatsInner,
)
from sendgrid.rest.api.suppressions.v3.models.invalid_email import InvalidEmail
from sendgrid.rest.api.suppressions.v3.models.list_asm_suppression200_response_inner import (
    ListAsmSuppression200ResponseInner,
)
from sendgrid.rest.api.suppressions.v3.models.list_global_suppression200_response_inner import (
    ListGlobalSuppression200ResponseInner,
)
from sendgrid.rest.api.suppressions.v3.models.list_suppression_bounces_classifications200_response import (
    ListSuppressionBouncesClassifications200Response,
)
from sendgrid.rest.api.suppressions.v3.models.list_suppression_bounces_classifications200_response_result_inner import (
    ListSuppressionBouncesClassifications200ResponseResultInner,
)
from sendgrid.rest.api.suppressions.v3.models.list_suppression_bounces_classifications200_response_result_inner_stats_inner import (
    ListSuppressionBouncesClassifications200ResponseResultInnerStatsInner,
)
from sendgrid.rest.api.suppressions.v3.models.retrieve_a_global_suppression_response import (
    RetrieveAGlobalSuppressionResponse,
)
from sendgrid.rest.api.suppressions.v3.models.spam_reports_response_inner import (
    SpamReportsResponseInner,
)
from sendgrid.rest.api.suppressions.v3.models.suppression_group import SuppressionGroup
from sendgrid.rest.api.suppressions.v3.models.suppression_group_request_base_props import (
    SuppressionGroupRequestBaseProps,
)
from sendgrid.rest.api.suppressions.v3.models.suppressions_request import (
    SuppressionsRequest,
)
from sendgrid.rest.api.suppressions.v3.models.update_asm_group_request import (
    UpdateAsmGroupRequest,
)

__all__ = [
    "Accept",
    "Accept1",
    "AddSuppressionToAsmGroup201Response",
    "BlocksResponseInner",
    "BounceResponse",
    "Classification",
    "Classification1",
    "CreatAsmGroup201Response",
    "CreateGlobalSuppression201Response",
    "DeleteInvalidEmailsRequest",
    "DeleteSpamReportsRequest",
    "DeleteSuppressionBlocksRequest",
    "DeleteSuppressionBouncesRequest",
    "ErrorResponse",
    "ErrorResponseErrorsInner",
    "GetAsmGroup200Response",
    "GetAsmSuppression200Response",
    "GetAsmSuppression200ResponseSuppressionsInner",
    "GetSuppressionBouncesClassifications200Response",
    "GetSuppressionBouncesClassifications200ResponseResultInner",
    "GetSuppressionBouncesClassifications200ResponseResultInnerStatsInner",
    "InvalidEmail",
    "ListAsmSuppression200ResponseInner",
    "ListGlobalSuppression200ResponseInner",
    "ListSuppressionBouncesClassifications200Response",
    "ListSuppressionBouncesClassifications200ResponseResultInner",
    "ListSuppressionBouncesClassifications200ResponseResultInnerStatsInner",
    "RetrieveAGlobalSuppressionResponse",
    "SpamReportsResponseInner",
    "SuppressionGroup",
    "SuppressionGroupRequestBaseProps",
    "SuppressionsRequest",
    "UpdateAsmGroupRequest",
]
# Testing code
