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
import warnings
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated
from sendgrid.base import values
from sendgrid.exceptions import ApiException
from sendgrid.http.request import Request
from sendgrid.http.response import ApiResponse

from pydantic import StrictStr

class VerifySenderToken:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            token: str,

    ):
        path='/v3/verified_senders/verify/{token}'
        path = path.format(
        token=token,
        )

        data = None
        request = Request(
            method='GET',
            url=path,
            data=data,
            headers=headers
        )
        response=self.client.send(request)
        if response is None:
            raise ApiException(error="CreateAlert creation failed: Unable to connect to server")

        if response.text:
            text = json.loads(response.text)
        else:
            text = ""
        if response.is_success():
            return ApiResponse(status_code=response.status_code, model=text, headers=response.headers)
        else:
            raise ApiException(status_code=response.status_code, error=text, headers=response.headers)