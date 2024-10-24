"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid IP Address API
  The Twilio SendGrid IP Address API allows you to add and manage dedicated IP addresses and IP Pools for your SendGrid account and Subusers. If you are sending any significant amount of email, SendGrid typically suggests sending from dedicated IPs. It's also best to send marketing and transactional emails from separate IP addresses. In order to do this, you'll need to set up IP Pools, which are groups of dedicated IP addresses you define to send particular types of messages. See the [**Dedicated IP Addresses**](https://docs.sendgrid.com/ui/account-and-settings/dedicated-ip-addresses) for more information about obtaining and allocating IPs.
 
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

from sendgrid.rest.api.ips.v3.models.list_assigned_ip200_response_inner import ListAssignedIp200ResponseInner

class ListAssignedIp:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
        
    ):
        path='/v3/ips/assigned'

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
