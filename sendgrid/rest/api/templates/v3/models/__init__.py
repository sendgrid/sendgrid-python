"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Templates API
  The Twilio SendGrid Templates API allows you to create and manage email templates to be delivered with SendGrid's sending APIs. The templates you create will be available using a template ID that is passed to our sending APIs as part of the request. Each template may then have multiple versions associated with it. Whichever version is set as \"active\" at the time of the request will be sent to your recipients. This system allows you to update a single template's look and feel entirely without modifying your requests to our Mail Send API. For example, you could have a single template for welcome emails. That welcome template could then have a version for each season of the year that's themed appropriately and marked as active during the appropriate season. The template ID passed to our sending APIs never needs to change; you can just modify which version is active.  This API provides operations to create and manage your templates as well as their versions.  Each user can create up to 300 different templates. Templates are specific to accounts and Subusers. Templates created on a parent account will not be accessible from the Subusers' accounts.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""


# import models into model package
from sendgrid.rest.api.templates.v3.models.active import Active
from sendgrid.rest.api.templates.v3.models.active1 import Active1
from sendgrid.rest.api.templates.v3.models.create_template_request import CreateTemplateRequest
from sendgrid.rest.api.templates.v3.models.duplicate_template_request import DuplicateTemplateRequest
from sendgrid.rest.api.templates.v3.models.editor import Editor
from sendgrid.rest.api.templates.v3.models.editor1 import Editor1
from sendgrid.rest.api.templates.v3.models.generation import Generation
from sendgrid.rest.api.templates.v3.models.generation1 import Generation1
from sendgrid.rest.api.templates.v3.models.generations import Generations
from sendgrid.rest.api.templates.v3.models.list_template200_response import ListTemplate200Response
from sendgrid.rest.api.templates.v3.models.list_template400_response import ListTemplate400Response
from sendgrid.rest.api.templates.v3.models.list_template400_response_errors_inner import ListTemplate400ResponseErrorsInner
from sendgrid.rest.api.templates.v3.models.metadata import Metadata
from sendgrid.rest.api.templates.v3.models.transactional_template import TransactionalTemplate
from sendgrid.rest.api.templates.v3.models.transactional_template_version_create import TransactionalTemplateVersionCreate
from sendgrid.rest.api.templates.v3.models.transactional_template_version_output import TransactionalTemplateVersionOutput
from sendgrid.rest.api.templates.v3.models.transactional_template_warning import TransactionalTemplateWarning
from sendgrid.rest.api.templates.v3.models.transactional_templates_template_lean import TransactionalTemplatesTemplateLean
from sendgrid.rest.api.templates.v3.models.transactional_templates_version_output_lean import TransactionalTemplatesVersionOutputLean
from sendgrid.rest.api.templates.v3.models.update_template_request import UpdateTemplateRequest
__all__ = [ 'Active',   'Active1',   'CreateTemplateRequest',   'DuplicateTemplateRequest',   'Editor',   'Editor1',   'Generation',   'Generation1',   'Generations',   'ListTemplate200Response',   'ListTemplate400Response',   'ListTemplate400ResponseErrorsInner',   'Metadata',   'TransactionalTemplate',   'TransactionalTemplateVersionCreate',   'TransactionalTemplateVersionOutput',   'TransactionalTemplateWarning',   'TransactionalTemplatesTemplateLean',   'TransactionalTemplatesVersionOutputLean',   'UpdateTemplateRequest'  ]
# Testing code