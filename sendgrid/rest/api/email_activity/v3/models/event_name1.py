from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class EventName1(Enum):
        BOUNCED='bounced'
        OPENED='opened'
        CLICKED='clicked'
        PROCESSED='processed'
        DROPPED='dropped'
        DELIVERED='delivered'
        DEFERRED='deferred'
        SPAM_REPORT='spam_report'
        UNSUBSCRIBE='unsubscribe'
        GROUP_UNSUBSCRIBE='group_unsubscribe'
        GROUP_RESUBSCRIBE='group_resubscribe'

