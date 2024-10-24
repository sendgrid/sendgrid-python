"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Marketing Campaigns Lists API
  The Twilio SendGrid Marketing Campaigns Lists API allows you to manage your contacts lists programmatically. Lists are static collections of Marketing Campaigns contacts. You can use this API to interact with the list objects themselves. To add contacts to a list, you must use the [Contacts API](https://docs.sendgrid.com/api-reference/contacts/).  You can also manage your lists using the Contacts menu in the [Marketing Campaigns application user interface](https://mc.sendgrid.com/contacts). For more information about lists and best practices for building them, see [**Building your Contact Lists**](https://sendgrid.com/docs/ui/managing-contacts/building-your-contact-list/).
 
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
from typing import Optional, Union
from typing_extensions import Annotated
from sendgrid.rest.api.mc_lists.v3.models.list_marketing_list200_response import ListMarketingList200Response

class ListMarketingList:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            page_size: Optional[float] = None,
    page_token: Optional[str] = None,

    ):
        path='/v3/marketing/lists'

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
