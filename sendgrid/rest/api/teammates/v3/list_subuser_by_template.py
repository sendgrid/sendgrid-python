"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Teammates API
  The Twilio SendGrid Teammates API allows you to add, manage, and remove Teammates, or user accounts, from your SendGrid account. Teammates function like user accounts on the SendGrid account, allowing you to invite additional users to your account with scoped access. You can think of Teammates as SendGrid's approach to enabling [role-based access control](https://en.wikipedia.org/wiki/Role-based_access_control) for your SendGrid account. For even more control over the access to your account, see the [Twilio SendGrid SSO API](https://docs.sendgrid.com/api-reference/single-sign-on-teammates/), which enables SSO-authenticated Teammates to be managed through a SAML 2.0 identity provider.
 
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
from sendgrid.rest.api.teammates.v3.models.list_subuser_by_template200_response import ListSubuserByTemplate200Response

class ListSubuserByTemplate:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            teammate_name: str,
    after_subuser_id: Optional[int] = None,
    limit: Optional[int] = None,
    username: Optional[str] = None,

    ):
        path='/v3/teammates/{teammate_name}/subuser_access'
        path = path.format(
        teammate_name=teammate_name,
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