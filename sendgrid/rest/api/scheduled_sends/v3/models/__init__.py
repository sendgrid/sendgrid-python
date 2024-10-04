"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Scheduled Sends API
  The Twilio SendGrid Scheduled Sends API allows you to cancel or pause the send of one or more emails using a batch ID.  A `batch_id` groups multiple scheduled mail send requests together with the same ID. You can cancel or pause all of the requests associated with a batch ID up to 10 minutes before the scheduled send time.  See [**Canceling a Scheduled Send**](https://docs.sendgrid.com/for-developers/sending-email/stopping-a-scheduled-send) for a guide on creating a `batch_id`, assigning it to a scheduled send, and modifying the send.  See the Mail API's batching operations to validate a `batch_id` and retrieve all scheduled sends as an array.  When a batch is canceled, all messages associated with that batch will stay in your sending queue. When their `send_at` value is reached, they will be discarded.  When a batch is paused, all messages associated with that batch will stay in your sending queue, even after their `send_at` value has passed. This means you can remove a pause status, and your scheduled send will be delivered once the pause is removed. Any messages left with a pause status that are more than 72 hours old will be discarded as Expired.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""


# import models into model package
from sendgrid.rest.api.scheduled_sends.v3.models.cancel_or_pause_a_scheduled_send_request import CancelOrPauseAScheduledSendRequest
from sendgrid.rest.api.scheduled_sends.v3.models.error_response import ErrorResponse
from sendgrid.rest.api.scheduled_sends.v3.models.error_response_errors_inner import ErrorResponseErrorsInner
from sendgrid.rest.api.scheduled_sends.v3.models.mail_batch_id import MailBatchId
from sendgrid.rest.api.scheduled_sends.v3.models.scheduled_send_status import ScheduledSendStatus
from sendgrid.rest.api.scheduled_sends.v3.models.status import Status
from sendgrid.rest.api.scheduled_sends.v3.models.status1 import Status1
from sendgrid.rest.api.scheduled_sends.v3.models.status2 import Status2
from sendgrid.rest.api.scheduled_sends.v3.models.update_scheduled_send_request import UpdateScheduledSendRequest
__all__ = [ 'CancelOrPauseAScheduledSendRequest',   'ErrorResponse',   'ErrorResponseErrorsInner',   'MailBatchId',   'ScheduledSendStatus',   'Status',   'Status1',   'Status2',   'UpdateScheduledSendRequest'  ]
# Testing code