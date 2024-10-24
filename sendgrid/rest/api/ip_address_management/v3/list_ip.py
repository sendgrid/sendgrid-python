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

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Optional
from typing_extensions import Annotated
from sendgrid.rest.api.ip_address_management.v3.models.list_ip200_response import ListIp200Response
from sendgrid.rest.api.ip_address_management.v3.models.region7 import Region7

class ListIp:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            ip: Optional[str] = None,
    limit: Optional[int] = None,
    after_key: Optional[int] = None,
    before_key: Optional[str] = None,
    is_leased: Optional[bool] = None,
    is_enabled: Optional[bool] = None,
    is_parent_assigned: Optional[bool] = None,
    pool: Optional[str] = None,
    start_added_at: Optional[int] = None,
    end_added_at: Optional[int] = None,
    region: Optional[Region7] = None,
    include_region: Optional[bool] = None,

    ):
        path='/v3/send_ips/ips'

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
