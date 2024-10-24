"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Webhook Configuration API
  The Twilio SendGrid Webhooks API allows you to configure the Event and Parse Webhooks.  Email is a data-rich channel, and implementing the Event Webhook will allow you to consume those data in nearly real time. This means you can actively monitor and participate in the health of your email program throughout the send cycle.  The Inbound Parse Webhook processes all incoming email for a domain or subdomain, parses the contents and attachments and then POSTs `multipart/form-data` to a URL that you choose.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""


# import models into model package
from sendgrid.rest.api.webhooks.v3.models.aggregated_by import AggregatedBy
from sendgrid.rest.api.webhooks.v3.models.create_event_webhook400_response import CreateEventWebhook400Response
from sendgrid.rest.api.webhooks.v3.models.create_event_webhook400_response_errors_inner import CreateEventWebhook400ResponseErrorsInner
from sendgrid.rest.api.webhooks.v3.models.error_response import ErrorResponse
from sendgrid.rest.api.webhooks.v3.models.error_response_errors_inner import ErrorResponseErrorsInner
from sendgrid.rest.api.webhooks.v3.models.event_webhook_all_response import EventWebhookAllResponse
from sendgrid.rest.api.webhooks.v3.models.event_webhook_base_response_props import EventWebhookBaseResponseProps
from sendgrid.rest.api.webhooks.v3.models.event_webhook_date_response_props import EventWebhookDateResponseProps
from sendgrid.rest.api.webhooks.v3.models.event_webhook_no_dates_response import EventWebhookNoDatesResponse
from sendgrid.rest.api.webhooks.v3.models.event_webhook_oauth_response_props import EventWebhookOauthResponseProps
from sendgrid.rest.api.webhooks.v3.models.event_webhook_request import EventWebhookRequest
from sendgrid.rest.api.webhooks.v3.models.event_webhook_signed_response import EventWebhookSignedResponse
from sendgrid.rest.api.webhooks.v3.models.event_webhook_signed_response_prop import EventWebhookSignedResponseProp
from sendgrid.rest.api.webhooks.v3.models.event_webhook_test_request import EventWebhookTestRequest
from sendgrid.rest.api.webhooks.v3.models.event_webhook_unsigned_response import EventWebhookUnsignedResponse
from sendgrid.rest.api.webhooks.v3.models.get_signed_event_webhook200_response import GetSignedEventWebhook200Response
from sendgrid.rest.api.webhooks.v3.models.get_signed_event_webhook404_response import GetSignedEventWebhook404Response
from sendgrid.rest.api.webhooks.v3.models.get_signed_event_webhook404_response_errors_inner import GetSignedEventWebhook404ResponseErrorsInner
from sendgrid.rest.api.webhooks.v3.models.list_parse_setting200_response import ListParseSetting200Response
from sendgrid.rest.api.webhooks.v3.models.list_parse_static200_response_inner import ListParseStatic200ResponseInner
from sendgrid.rest.api.webhooks.v3.models.list_parse_static200_response_inner_stats_inner import ListParseStatic200ResponseInnerStatsInner
from sendgrid.rest.api.webhooks.v3.models.list_parse_static200_response_inner_stats_inner_metrics import ListParseStatic200ResponseInnerStatsInnerMetrics
from sendgrid.rest.api.webhooks.v3.models.parse_setting import ParseSetting
from sendgrid.rest.api.webhooks.v3.models.update_signed_event_webhook_request import UpdateSignedEventWebhookRequest
__all__ = [ 'AggregatedBy',   'CreateEventWebhook400Response',   'CreateEventWebhook400ResponseErrorsInner',   'ErrorResponse',   'ErrorResponseErrorsInner',   'EventWebhookAllResponse',   'EventWebhookBaseResponseProps',   'EventWebhookDateResponseProps',   'EventWebhookNoDatesResponse',   'EventWebhookOauthResponseProps',   'EventWebhookRequest',   'EventWebhookSignedResponse',   'EventWebhookSignedResponseProp',   'EventWebhookTestRequest',   'EventWebhookUnsignedResponse',   'GetSignedEventWebhook200Response',   'GetSignedEventWebhook404Response',   'GetSignedEventWebhook404ResponseErrorsInner',   'ListParseSetting200Response',   'ListParseStatic200ResponseInner',   'ListParseStatic200ResponseInnerStatsInner',   'ListParseStatic200ResponseInnerStatsInnerMetrics',   'ParseSetting',   'UpdateSignedEventWebhookRequest'  ]
# Testing code