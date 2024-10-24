"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid IP Address Management API
  The Twilio SendGrid IP Address Management API combines functionality that was previously split between the Twilio SendGrid [IP Address API](https://docs.sendgrid.com/api-reference/ip-address) and [IP Pools API](https://docs.sendgrid.com/api-reference/ip-pools). This functionality includes adding IP addresses to your account, assigning IP addresses to IP Pools and Subusers, among other tasks.
 
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
from sendgrid.rest.api.ip_address_management.v3.models.add_sub_users_to_ip200_response import AddSubUsersToIp200Response
from sendgrid.rest.api.ip_address_management.v3.models.add_sub_users_to_ip_request import AddSubUsersToIpRequest

class AddSubUsersToIp:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            ip: str,
    add_sub_users_to_ip_request: Optional[AddSubUsersToIpRequest] = None,

    ):
        path='/v3/send_ips/ips/{ip}/subusers:batchAdd'
        path = path.format(
        ip=ip,
        )

        data = None
        if add_sub_users_to_ip_request:
            data = add_sub_users_to_ip_request.to_dict()
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