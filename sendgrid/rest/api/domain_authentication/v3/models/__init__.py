"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Domain Authentication API
  The Twilio SendGrid Domain Authentication API allows you to manage your authenticated domains and their settings.  Domain Authentication is a required step when setting up your Twilio SendGrid account because it's essential to ensuring the deliverability of your email. Domain Authentication signals trustworthiness to email inbox providers and your recipients by approving SendGrid to send email on behalf of your domain. For more information, see [**How to Set Up Domain Authentication**](https://sendgrid.com/docs/ui/account-and-settings/how-to-set-up-domain-authentication/).  Each user may have a maximum of 3,000 authenticated domains and 3,000 link brandings. This limit is at the user level, meaning each Subuser belonging to a parent account may have its own 3,000 authenticated domains and 3,000 link brandings.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""

# import models into model package
from sendgrid.rest.api.domain_authentication.v3.models.add_ip_to_authenticated_domain_request import (
    AddIpToAuthenticatedDomainRequest,
)
from sendgrid.rest.api.domain_authentication.v3.models.associate_subuser_with_domain_request import (
    AssociateSubuserWithDomainRequest,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticate_domain_request import (
    AuthenticateDomainRequest,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain import (
    AuthenticatedDomain,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf import (
    AuthenticatedDomainSpf,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns import (
    AuthenticatedDomainSpfDns,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_dkim import (
    AuthenticatedDomainSpfDnsDkim,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_domain_spf import (
    AuthenticatedDomainSpfDnsDomainSpf,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_mail_server import (
    AuthenticatedDomainSpfDnsMailServer,
)
from sendgrid.rest.api.domain_authentication.v3.models.authenticated_domain_spf_dns_subdomain_spf import (
    AuthenticatedDomainSpfDnsSubdomainSpf,
)
from sendgrid.rest.api.domain_authentication.v3.models.email_dns_record400_response import (
    EmailDnsRecord400Response,
)
from sendgrid.rest.api.domain_authentication.v3.models.email_dns_record400_response_errors import (
    EmailDnsRecord400ResponseErrors,
)
from sendgrid.rest.api.domain_authentication.v3.models.email_dns_record_request import (
    EmailDnsRecordRequest,
)
from sendgrid.rest.api.domain_authentication.v3.models.list_all_authenticated_domain_with_user200_response_inner import (
    ListAllAuthenticatedDomainWithUser200ResponseInner,
)
from sendgrid.rest.api.domain_authentication.v3.models.list_all_authenticated_domain_with_user200_response_inner_dns import (
    ListAllAuthenticatedDomainWithUser200ResponseInnerDns,
)
from sendgrid.rest.api.domain_authentication.v3.models.list_all_authenticated_domain_with_user200_response_inner_dns_dkim1 import (
    ListAllAuthenticatedDomainWithUser200ResponseInnerDnsDkim1,
)
from sendgrid.rest.api.domain_authentication.v3.models.list_all_authenticated_domain_with_user200_response_inner_dns_mail_cname import (
    ListAllAuthenticatedDomainWithUser200ResponseInnerDnsMailCname,
)
from sendgrid.rest.api.domain_authentication.v3.models.update_authenticated_domain_request import (
    UpdateAuthenticatedDomainRequest,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response import (
    ValidateAuthenticatedDomain200Response,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results import (
    ValidateAuthenticatedDomain200ResponseValidationResults,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results_dkim1 import (
    ValidateAuthenticatedDomain200ResponseValidationResultsDkim1,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results_mail_cname import (
    ValidateAuthenticatedDomain200ResponseValidationResultsMailCname,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain200_response_validation_results_spf import (
    ValidateAuthenticatedDomain200ResponseValidationResultsSpf,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain500_response import (
    ValidateAuthenticatedDomain500Response,
)
from sendgrid.rest.api.domain_authentication.v3.models.validate_authenticated_domain500_response_errors_inner import (
    ValidateAuthenticatedDomain500ResponseErrorsInner,
)

__all__ = [
    "AddIpToAuthenticatedDomainRequest",
    "AssociateSubuserWithDomainRequest",
    "AuthenticateDomainRequest",
    "AuthenticatedDomain",
    "AuthenticatedDomainSpf",
    "AuthenticatedDomainSpfDns",
    "AuthenticatedDomainSpfDnsDkim",
    "AuthenticatedDomainSpfDnsDomainSpf",
    "AuthenticatedDomainSpfDnsMailServer",
    "AuthenticatedDomainSpfDnsSubdomainSpf",
    "EmailDnsRecord400Response",
    "EmailDnsRecord400ResponseErrors",
    "EmailDnsRecordRequest",
    "ListAllAuthenticatedDomainWithUser200ResponseInner",
    "ListAllAuthenticatedDomainWithUser200ResponseInnerDns",
    "ListAllAuthenticatedDomainWithUser200ResponseInnerDnsDkim1",
    "ListAllAuthenticatedDomainWithUser200ResponseInnerDnsMailCname",
    "UpdateAuthenticatedDomainRequest",
    "ValidateAuthenticatedDomain200Response",
    "ValidateAuthenticatedDomain200ResponseValidationResults",
    "ValidateAuthenticatedDomain200ResponseValidationResultsDkim1",
    "ValidateAuthenticatedDomain200ResponseValidationResultsMailCname",
    "ValidateAuthenticatedDomain200ResponseValidationResultsSpf",
    "ValidateAuthenticatedDomain500Response",
    "ValidateAuthenticatedDomain500ResponseErrorsInner",
]
# Testing code
