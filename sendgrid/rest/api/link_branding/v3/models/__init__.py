"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Link Branding API
  The Twilio SendGrid Link Branding API allows you to configure your domain settings so that all of the click-tracked links, opens, and images in your emails are served from your domain rather than `sendgrid.net`. Spam filters and recipient servers look at the links within emails to determine whether the email appear trustworthy. They use the reputation of the root domain to determine whether the links can be trusted.  You can also manage Link Branding in the **Sender Authentication** section of the Twilio SendGrid application user interface.   See [**How to Set Up Link Branding**](https: //sendgrid.com/docs/ui/account-and-settings/how-to-set-up-link-branding/) for more information.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""


# import models into model package
from sendgrid.rest.api.link_branding.v3.models.associate_branded_link_with_subuser_request import AssociateBrandedLinkWithSubuserRequest
from sendgrid.rest.api.link_branding.v3.models.create_branded_link_request import CreateBrandedLinkRequest
from sendgrid.rest.api.link_branding.v3.models.default import Default
from sendgrid.rest.api.link_branding.v3.models.default1 import Default1
from sendgrid.rest.api.link_branding.v3.models.default2 import Default2
from sendgrid.rest.api.link_branding.v3.models.legacy import Legacy
from sendgrid.rest.api.link_branding.v3.models.link_branding200 import LinkBranding200
from sendgrid.rest.api.link_branding.v3.models.link_branding200_dns import LinkBranding200Dns
from sendgrid.rest.api.link_branding.v3.models.link_branding200_dns_domain_cname import LinkBranding200DnsDomainCname
from sendgrid.rest.api.link_branding.v3.models.link_branding200_dns_owner_cname import LinkBranding200DnsOwnerCname
from sendgrid.rest.api.link_branding.v3.models.region import Region
from sendgrid.rest.api.link_branding.v3.models.type import Type
from sendgrid.rest.api.link_branding.v3.models.type1 import Type1
from sendgrid.rest.api.link_branding.v3.models.update_branded_link_request import UpdateBrandedLinkRequest
from sendgrid.rest.api.link_branding.v3.models.valid import Valid
from sendgrid.rest.api.link_branding.v3.models.valid1 import Valid1
from sendgrid.rest.api.link_branding.v3.models.valid2 import Valid2
from sendgrid.rest.api.link_branding.v3.models.valid3 import Valid3
from sendgrid.rest.api.link_branding.v3.models.valid4 import Valid4
from sendgrid.rest.api.link_branding.v3.models.valid5 import Valid5
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link200_response import ValidateBrandedLink200Response
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link200_response_validation_results import ValidateBrandedLink200ResponseValidationResults
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link200_response_validation_results_domain_cname import ValidateBrandedLink200ResponseValidationResultsDomainCname
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link200_response_validation_results_owner_cname import ValidateBrandedLink200ResponseValidationResultsOwnerCname
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link500_response import ValidateBrandedLink500Response
from sendgrid.rest.api.link_branding.v3.models.validate_branded_link500_response_errors_inner import ValidateBrandedLink500ResponseErrorsInner
__all__ = [ 'AssociateBrandedLinkWithSubuserRequest',   'CreateBrandedLinkRequest',   'Default',   'Default1',   'Default2',   'Legacy',   'LinkBranding200',   'LinkBranding200Dns',   'LinkBranding200DnsDomainCname',   'LinkBranding200DnsOwnerCname',   'Region',   'Type',   'Type1',   'UpdateBrandedLinkRequest',   'Valid',   'Valid1',   'Valid2',   'Valid3',   'Valid4',   'Valid5',   'ValidateBrandedLink200Response',   'ValidateBrandedLink200ResponseValidationResults',   'ValidateBrandedLink200ResponseValidationResultsDomainCname',   'ValidateBrandedLink200ResponseValidationResultsOwnerCname',   'ValidateBrandedLink500Response',   'ValidateBrandedLink500ResponseErrorsInner'  ]
# Testing code