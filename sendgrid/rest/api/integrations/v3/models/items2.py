from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Items2(Enum):
        DROP='drop'
        PROCESSED='processed'
        DEFERRED='deferred'
        GROUP_UNSUBSCRIBE='group_unsubscribe'
        BOUNCE='bounce'
        DELIVERED='delivered'
        CLICK='click'
        UNSUBSCRIBE='unsubscribe'
        OPEN='open'
        GROUP_RESUBSCRIBE='group_resubscribe'
        SPAMREPORT='spamreport'
        MACHINE_OPENED='machine_opened'

