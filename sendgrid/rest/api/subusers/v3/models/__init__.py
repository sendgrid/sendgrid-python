"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Subusers
  The Twilio SendGrid Subusers API allows you to create and manage your Subuser accounts. Subusers are available on [Pro and Premier plans](https://sendgrid.com/pricing), and you can think of them as sub-accounts. Each Subuser can have its own sending domains, IP addresses, and reporting. SendGrid recommends creating Subusers for each of the different types of emails you send—one Subuser for transactional emails and another for marketing emails. Independent Software Vendor (ISV) customers may also create Subusers for each of their customers.  You can also manage Subusers in the [Twilio SendGrid application user interface](https://app.sendgrid.com/settings/subusers). See [**Subusers**](https://docs.sendgrid.com/ui/account-and-settings/subusers) for more information.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""


# import models into model package
from sendgrid.rest.api.subusers.v3.models.aggregated_by import AggregatedBy
from sendgrid.rest.api.subusers.v3.models.category_stats import CategoryStats
from sendgrid.rest.api.subusers.v3.models.category_stats_stats_inner import CategoryStatsStatsInner
from sendgrid.rest.api.subusers.v3.models.category_stats_stats_inner_metrics import CategoryStatsStatsInnerMetrics
from sendgrid.rest.api.subusers.v3.models.create_subuser_request import CreateSubuserRequest
from sendgrid.rest.api.subusers.v3.models.error_response import ErrorResponse
from sendgrid.rest.api.subusers.v3.models.error_response_errors_inner import ErrorResponseErrorsInner
from sendgrid.rest.api.subusers.v3.models.list_reputation200_response_inner import ListReputation200ResponseInner
from sendgrid.rest.api.subusers.v3.models.region import Region
from sendgrid.rest.api.subusers.v3.models.region1 import Region1
from sendgrid.rest.api.subusers.v3.models.region2 import Region2
from sendgrid.rest.api.subusers.v3.models.region3 import Region3
from sendgrid.rest.api.subusers.v3.models.reset_frequency import ResetFrequency
from sendgrid.rest.api.subusers.v3.models.reset_frequency1 import ResetFrequency1
from sendgrid.rest.api.subusers.v3.models.sort_by_direction import SortByDirection
from sendgrid.rest.api.subusers.v3.models.sort_by_direction1 import SortByDirection1
from sendgrid.rest.api.subusers.v3.models.sort_by_direction2 import SortByDirection2
from sendgrid.rest.api.subusers.v3.models.sort_by_metric import SortByMetric
from sendgrid.rest.api.subusers.v3.models.subuser import Subuser
from sendgrid.rest.api.subusers.v3.models.subuser_credits import SubuserCredits
from sendgrid.rest.api.subusers.v3.models.subuser_credits_request import SubuserCreditsRequest
from sendgrid.rest.api.subusers.v3.models.subuser_post import SubuserPost
from sendgrid.rest.api.subusers.v3.models.subuser_post_credit_allocation import SubuserPostCreditAllocation
from sendgrid.rest.api.subusers.v3.models.subuser_stats import SubuserStats
from sendgrid.rest.api.subusers.v3.models.subuser_stats_stats_inner import SubuserStatsStatsInner
from sendgrid.rest.api.subusers.v3.models.subuser_stats_stats_inner_metrics import SubuserStatsStatsInnerMetrics
from sendgrid.rest.api.subusers.v3.models.type import Type
from sendgrid.rest.api.subusers.v3.models.type1 import Type1
from sendgrid.rest.api.subusers.v3.models.update_subuser_ip200_response import UpdateSubuserIp200Response
from sendgrid.rest.api.subusers.v3.models.update_subuser_remaining_credit_request import UpdateSubuserRemainingCreditRequest
from sendgrid.rest.api.subusers.v3.models.update_subuser_request import UpdateSubuserRequest
from sendgrid.rest.api.subusers.v3.models.update_subuser_website_access_request import UpdateSubuserWebsiteAccessRequest
__all__ = [ 'AggregatedBy',   'CategoryStats',   'CategoryStatsStatsInner',   'CategoryStatsStatsInnerMetrics',   'CreateSubuserRequest',   'ErrorResponse',   'ErrorResponseErrorsInner',   'ListReputation200ResponseInner',   'Region',   'Region1',   'Region2',   'Region3',   'ResetFrequency',   'ResetFrequency1',   'SortByDirection',   'SortByDirection1',   'SortByDirection2',   'SortByMetric',   'Subuser',   'SubuserCredits',   'SubuserCreditsRequest',   'SubuserPost',   'SubuserPostCreditAllocation',   'SubuserStats',   'SubuserStatsStatsInner',   'SubuserStatsStatsInnerMetrics',   'Type',   'Type1',   'UpdateSubuserIp200Response',   'UpdateSubuserRemainingCreditRequest',   'UpdateSubuserRequest',   'UpdateSubuserWebsiteAccessRequest'  ]
# Testing code