"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Link Branding API
  The Twilio SendGrid Link Branding API allows you to configure your domain settings so that all of the click-tracked links, opens, and images in your emails are served from your domain rather than `sendgrid.net`. Spam filters and recipient servers look at the links within emails to determine whether the email appear trustworthy. They use the reputation of the root domain to determine whether the links can be trusted.  You can also manage Link Branding in the **Sender Authentication** section of the Twilio SendGrid application user interface.   See [**How to Set Up Link Branding**](https: //sendgrid.com/docs/ui/account-and-settings/how-to-set-up-link-branding/) for more information.
 
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

from pydantic import Field, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link200_response import ValidateBrandedLink200Response

class ValidateBrandedLink:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            id: int,
    on_behalf_of: Optional[str] = None,

    ):
        path='/v3/whitelabel/links/{id}/validate'
        path = path.format(
        id=id,
        )

        headers = values.of(
        {
            'on-behalf-of': on_behalf_of,
        })
        data = None
        request = Request(
            method='POST',
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
