"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Scopes API
  The Twilio SendGrid Scopes API allows you to retrieve the scopes or permissions available to a user, see the user's attempts to access your SendGrid account, and, if necessary, deny an access request.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

import json
from typing import Optional
from sendgrid.base import values
from sendgrid.exceptions import ApiException
from sendgrid.http.request import Request
from sendgrid.http.response import ApiResponse

from typing import Optional


class ListScope:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        on_behalf_of: Optional[str] = None,
    ):
        path = "/v3/scopes"

        headers = values.of(
            {
                "on-behalf-of": on_behalf_of,
            }
        )
        data = None
        request = Request(method="GET", url=path, data=data, headers=headers)
        response = self.client.send(request)
        if response is None:
            raise ApiException(
                error="CreateAlert creation failed: Unable to connect to server"
            )

        if response.text:
            text = json.loads(response.text)
        else:
            text = ""
        if response.is_success():
            return ApiResponse(
                status_code=response.status_code, model=text, headers=response.headers
            )
        else:
            raise ApiException(
                status_code=response.status_code, error=text, headers=response.headers
            )
