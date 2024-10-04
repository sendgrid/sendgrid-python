"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Verified Senders API
  The Twilio SendGrid Verified Senders API allows you to programmatically manage the Sender Identities that are authorized to send email for your account. You can also manage Sender Identities in the [SendGrid application user interface](https://app.sendgrid.com/settings/sender_auth). See [**Single Sender Verification**](https://sendgrid.com/docs/ui/sending-email/sender-verification/) for more information.  You an use this API to create new Sender Identities, retrieve a list of existing Sender Identities, check the status of a Sender Identity, update a Sender Identity, and delete a Sender Identity.  This API offers additional operations to check for domains known to implement DMARC and resend verification emails to Sender Identities that have yet to complete the verification process.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

import json
from typing import Optional
from sendgrid.exceptions import ApiException
from sendgrid.http.request import Request
from sendgrid.http.response import ApiResponse

from typing import Optional
from sendgrid.rest.api.verified_senders.v3.models.verified_sender_request import (
    VerifiedSenderRequest,
)


class UpdateVerifiedSender:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        id: str,
        verified_sender_request: Optional[VerifiedSenderRequest] = None,
    ):
        path = "/v3/verified_senders/{id}"
        path = path.format(
            id=id,
        )

        data = None
        if verified_sender_request:
            data = verified_sender_request.to_dict()
        request = Request(method="PATCH", url=path, data=data, headers=headers)
        response = self.client.send(request)
        if response is None:
            raise ApiException(
                error="CreateAlert creation failed: Unable to connect to server"
            )

        if response.text:
            text = json.loads(response.text)
        else:
            text = ""
        if response.is_success():
            return ApiResponse(
                status_code=response.status_code, model=text, headers=response.headers
            )
        else:
            raise ApiException(
                status_code=response.status_code, error=text, headers=response.headers
            )
