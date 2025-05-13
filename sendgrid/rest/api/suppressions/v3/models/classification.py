from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Classification(Enum):
        CONTENT='Content'
        FREQUENCY_OR_VOLUME_TOO_HIGH='Frequency or Volume Too High'
        INVALID_ADDRESS='Invalid Address'
        MAILBOX_UNAVAILABLE='Mailbox Unavailable'
        REPUTATION='Reputation'
        TECHNICAL_FAILURE='Technical Failure'
        UNCLASSIFIED='Unclassified'

