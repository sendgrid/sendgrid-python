"""
  This code was generated by
 
  SENDGRID-OAI-GENERATOR
 
  Twilio SendGrid Engagement Quality API
  The SendGrid Engagement Quality (SEQ) API allows you to retrieve metrics that define the quality of your email program.  An SEQ score is correlated with: - The quality of the data in a sender’s program. - How “wanted” the sender's email is by their recipients.  Because “wanted” email and deliverability are closely related, a higher SEQ metric is correlated with greater deliverability. This means the higher your SEQ score, the more likely you are to land in your recipients' inboxes. See the SEQ Overview page to understand SEQ, how it's calculated, and how you can address your score. The SEQ endpoints allow you to retrieve your scores and scores for your Subusers.
 
  NOTE: This class is auto generated by OpenAPI Generator.
  https://openapi-generator.tech
  Do not edit the class manually.
"""


# import models into model package
from sendgrid.rest.api.seq.v3.models.seq_error import SeqError
from sendgrid.rest.api.seq.v3.models.seq_metadata import SeqMetadata
from sendgrid.rest.api.seq.v3.models.seq_metadata_next_params import SeqMetadataNextParams
from sendgrid.rest.api.seq.v3.models.seq_metrics import SeqMetrics
from sendgrid.rest.api.seq.v3.models.seq_score import SeqScore
__all__ = [ 'SeqError',   'SeqMetadata',   'SeqMetadataNextParams',   'SeqMetrics',   'SeqScore'  ]
# Testing code