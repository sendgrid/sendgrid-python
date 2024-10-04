from enum import Enum
from enum import Enum


class EventName(Enum):
    BOUNCED = "bounced"
    OPENED = "opened"
    CLICKED = "clicked"
    PROCESSED = "processed"
    DROPPED = "dropped"
    DELIVERED = "delivered"
    DEFERRED = "deferred"
    SPAM_REPORT = "spam_report"
    UNSUBSCRIBE = "unsubscribe"
    GROUP_UNSUBSCRIBE = "group_unsubscribe"
    GROUP_RESUBSCRIBE = "group_resubscribe"
