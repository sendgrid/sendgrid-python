"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid IP Access Management API
  IP Twilio SendGrid IP Access Management API allows you to control which IP addresses can be used to access your account, either through the SendGrid application user interface or the API.  There is no limit to the number of IP addresses that you can allow.  It is possible to remove your own IP address from your list of allowed addresses, thus blocking your own access to your account. While we are able to restore your access, we do require thorough proof of your identify and ownership of your account. We take the security of your account very seriously and wish to prevent any 'bad actors' from maliciously gaining access to your account. Your current IP is clearly displayed to help prevent you from accidentally removing it from the allowed addresses.  See [**IP Access Management**](https://docs.sendgrid.com/ui/account-and-settings/ip-access-management) for more information.
 
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
from sendgrid.rest.api.ip_access_management.v3.models.ip_access_management2xx import IpAccessManagement2xx

class ListAllowedIp:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            on_behalf_of: Optional[str] = None,

    ):
        path='/v3/access_settings/whitelist'

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
