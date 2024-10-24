"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Domain Authentication API
  The Twilio SendGrid Domain Authentication API allows you to manage your authenticated domains and their settings.  Domain Authentication is a required step when setting up your Twilio SendGrid account because it's essential to ensuring the deliverability of your email. Domain Authentication signals trustworthiness to email inbox providers and your recipients by approving SendGrid to send email on behalf of your domain. For more information, see [**How to Set Up Domain Authentication**](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-domain-authentication/).  Each user may have a maximum of 3,000 authenticated domains and 3,000 link brandings. This limit is at the user level, meaning each Subuser belonging to a parent account may have its own 3,000 authenticated domains and 3,000 link brandings.
 
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

from pydantic import Field, StrictStr
from typing import Optional
from typing_extensions import Annotated
from sendgrid.rest.api.domain_authentication.v3.models.update_authenticated_domain_request import UpdateAuthenticatedDomainRequest
from sendgrid.rest.api.domain_authentication.v3.models.object import object

class UpdateAuthenticatedDomain:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            domain_id: str,
    on_behalf_of: Optional[str] = None,
    update_authenticated_domain_request: Optional[UpdateAuthenticatedDomainRequest] = None,

    ):
        path='/v3/whitelabel/domains/{domain_id}'
        path = path.format(
        domain_id=domain_id,
        )

        headers = values.of(
        {
            'on-behalf-of': on_behalf_of,
        })
        headers["Content-Type"] = "application/json"
        data = None
        if update_authenticated_domain_request:
            data = update_authenticated_domain_request.to_dict()
        request = Request(
            method='PATCH',
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
