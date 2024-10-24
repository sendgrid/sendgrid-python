"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Reverse DNS API
  The Twilio SendGrid Reverse DNS API (formerly IP Whitelabel) allows you to configure reverse DNS settings for your account. Mailbox providers verify the sender of your emails by performing a reverse DNS lookup.  When setting up Reverse DNS, Twilio SendGrid will provide an A Record (address record) for you to add to the DNS records of your sending domain. The A record maps your sending domain to a dedicated Twilio SendGrid IP address. Once Twilio SendGrid has verified that the appropriate A record for the IP address has been created, the appropriate reverse DNS record for the IP address is generated.  Reverse DNS is available for [dedicated IP addresses](https://sendgrid.com/docs/ui/account-and-settings/dedicated-ip-addresses/) only.  You can also manage your reverse DNS settings in the Sender Authentication setion of the [Twilio SendGrid application user interface](https://app.sendgrid.com/settings/sender_auth).  See [**How to Set Up Reverse DNS**](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-reverse-dns/) for more information.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""


# import models into model package
from sendgrid.rest.api.reverse_dns.v3.models.reverse_dns import ReverseDns
from sendgrid.rest.api.reverse_dns.v3.models.reverse_dns_a_record import ReverseDnsARecord
from sendgrid.rest.api.reverse_dns.v3.models.reverse_dns_users_inner import ReverseDnsUsersInner
from sendgrid.rest.api.reverse_dns.v3.models.set_up_reverse_dns_request import SetUpReverseDnsRequest
from sendgrid.rest.api.reverse_dns.v3.models.valid import Valid
from sendgrid.rest.api.reverse_dns.v3.models.valid1 import Valid1
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns200_response import ValidateReverseDns200Response
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns200_response_validation_results import ValidateReverseDns200ResponseValidationResults
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns200_response_validation_results_a_record import ValidateReverseDns200ResponseValidationResultsARecord
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns404_response import ValidateReverseDns404Response
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns404_response_errors_inner import ValidateReverseDns404ResponseErrorsInner
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns500_response import ValidateReverseDns500Response
from sendgrid.rest.api.reverse_dns.v3.models.validate_reverse_dns500_response_errors_inner import ValidateReverseDns500ResponseErrorsInner
__all__ = [ 'ReverseDns',   'ReverseDnsARecord',   'ReverseDnsUsersInner',   'SetUpReverseDnsRequest',   'Valid',   'Valid1',   'ValidateReverseDns200Response',   'ValidateReverseDns200ResponseValidationResults',   'ValidateReverseDns200ResponseValidationResultsARecord',   'ValidateReverseDns404Response',   'ValidateReverseDns404ResponseErrorsInner',   'ValidateReverseDns500Response',   'ValidateReverseDns500ResponseErrorsInner'  ]
# Testing code