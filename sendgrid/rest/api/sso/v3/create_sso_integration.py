"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Single Sign-On API
  The Single Sign-On API allows you to manage your SAML 2.0 SSO configurations. You can also work with your SSO integrations using the SSO section of the [Twilio SendGrid application user interface](https://app.sendgrid.com/settings/sso).  The Single Sign-On Settings operations allow you to create, retrieve, modify, and delete SSO integrations for your Twilio SendGrid account. Each integration will correspond to a specific IdP such as Okta, Duo, or Microsoft Azure Active Directory.  The Single Sign-On Certificates operations allow you to create, modify, and delete SSO certificates. A SAML certificate allows your IdP and Twilio SendGrid to verify requests are coming from one another using the `public_certificate` and `integration_id` parameters.  The Single Sign-On Teammates operations allow you to add and modify SSO Teammates. SSO Teammates are the individual user accounts who will access your Twilio SendGrid account with SSO credentials. To retrieve or delete an SSO Teammate, you will use the separate [Teammates API](https://docs.sendgrid.com/api-reference/teammates/).
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

import json
from typing import Optional
from sendgrid.exceptions import ApiException
from sendgrid.http.request import Request
from sendgrid.http.response import ApiResponse

from typing import Optional
from sendgrid.rest.api.sso.v3.models.post_patch_integration_request import (
    PostPatchIntegrationRequest,
)


class CreateSsoIntegration:
    def __init__(self, client) -> None:
        self.client = client

    def send(
        self,
        post_patch_integration_request: Optional[PostPatchIntegrationRequest] = None,
    ):
        path = "/v3/sso/integrations"

        data = None
        if post_patch_integration_request:
            data = post_patch_integration_request.to_dict()
        request = Request(method="POST", url=path, data=data, headers=headers)
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
