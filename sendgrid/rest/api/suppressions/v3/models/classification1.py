from enum import Enum
from enum import Enum


class Classification1(Enum):
    CONTENT = "Content"
    FREQUENCY_OR_VOLUME_TOO_HIGH = "Frequency or Volume Too High"
    INVALID_ADDRESS = "Invalid Address"
    MAILBOX_UNAVAILABLE = "Mailbox Unavailable"
    REPUTATION = "Reputation"
    TECHNICAL_FAILURE = "Technical Failure"
    UNCLASSIFIED = "Unclassified"
