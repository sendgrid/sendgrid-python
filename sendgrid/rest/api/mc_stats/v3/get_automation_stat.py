"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Marketing Campaigns Statistics API
  The Marketing Campaigns Stats API allows you to retrieve statistics for both Automations and Single Sends. The statistics provided include bounces, clicks, opens, and more. You can export stats in CSV format for use in other applications. You can also retrieve Marketing Campaigns stats in the [Marketing Campaigns application user interface](https://mc.sendgrid.com/).  This API provides statistics for Marketing Campaigns only. For stats related to event tracking, please see the [Stats API](https://docs.sendgrid.com/api-reference/stats).
 
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

from datetime import date
from pydantic import Field, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from sendgrid.rest.api.mc_stats.v3.models.aggregated_by import AggregatedBy
from sendgrid.rest.api.mc_stats.v3.models.automations_response import AutomationsResponse
from sendgrid.rest.api.mc_stats.v3.models.items import Items

class GetAutomationStat:
    def __init__(self, client) -> None:
        self.client = client
    
    def send(
        self,
            id: str,
    group_by: Optional[List[Items]] = None,
    step_ids: Optional[List[str]] = None,
    aggregated_by: Optional[AggregatedBy] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    timezone: Optional[str] = None,
    page_size: Optional[int] = None,
    page_token: Optional[str] = None,

    ):
        path='/v3/marketing/stats/automations/{id}'
        path = path.format(
        id=id,
        )

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
