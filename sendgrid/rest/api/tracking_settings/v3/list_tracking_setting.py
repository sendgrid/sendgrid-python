"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Tracking Settings API
  The Twilio SendGrid Tracking Settings API allows you to configure which tracking settings are enabled for your messages. You can track many of your recipients' interactions with your emails, including which emails they open, which links they click, and when they subscribe to or unsubscribe from your emails. See [**Tracking Settings**](https://docs.sendgrid.com/ui/account-and-settings/tracking) for more information.
 
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
from sendgrid.rest.api.tracking_settings.v3.models.list_tracking_setting200_response import ListTrackingSetting200Response

class ListTrackingSetting:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            on_behalf_of: Optional[str] = None,

    ):
        path='/v3/tracking_settings'

        headers = values.of(
        {
            'on-behalf-of': on_behalf_of,
        })
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
