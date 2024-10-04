"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid User API
  The Twilio SendGrid User API allows you to modify the settings of a SendGrid user account such as the user's email address or username. Keeping your user profile up to date helps SendGrid verify who you are and share important communications with you.  See [**Account Details**](https://docs.sendgrid.com/ui/account-and-settings/account) for more information. You can also manage your user settings in the [SendGrid application user interface](https://app.sendgrid.com/account/details).
 
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
from sendgrid.rest.api.user.v3.models.update_username200_response import UpdateUsername200Response
from sendgrid.rest.api.user.v3.models.update_username_request import UpdateUsernameRequest

class UpdateUsername:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            on_behalf_of: Optional[str] = None,
    update_username_request: Optional[UpdateUsernameRequest] = None,

    ):
        path='/v3/user/username'

        headers = values.of(
        {
            'on-behalf-of': on_behalf_of,
        })
        headers["Content-Type"] = "application/json"
        data = None
        if update_username_request:
            data = update_username_request.to_dict()
        request = Request(
            method='PUT',
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
