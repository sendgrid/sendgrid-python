"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Legacy Marketing Campaigns Contacts API
  The Twilio SendGrid Legacy Marketing Campaigns Contacts API allows you to manage your marketing contacts programmatically. This API is operational, but we recommend using the current version of Marketing Campaigns' [Contacts API](https://docs.sendgrid.com/api-reference/contacts/), [Lists API](https://docs.sendgrid.com/api-reference/lists/), and [Segments API](https://docs.sendgrid.com/api-reference/segmenting-contacts-v2/) to manage your contacts.  See [**Migrating from Legacy Marketing Campaigns**](https://docs.sendgrid.com/ui/sending-email/migrating-from-legacy-marketing-campaigns) for more information.
 
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
from typing import Any, Optional
from typing_extensions import Annotated
from sendgrid.rest.api.lmc_contactdb.v3.models.delete_contacts import DeleteContacts

class DeleteContactDbList:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            list_id: int,
    on_behalf_of: Optional[str] = None,
    delete_contacts: Optional[DeleteContacts] = None,
    body: Optional[object] = None,

    ):
        path='/v3/contactdb/lists/{list_id}'
        path = path.format(
        list_id=list_id,
        )

        headers = values.of(
        {
            'on-behalf-of': on_behalf_of,
        })
        headers["Content-Type"] = "application/json"
        data = None
        if body:
            data = body.to_dict()
        request = Request(
            method='DELETE',
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
