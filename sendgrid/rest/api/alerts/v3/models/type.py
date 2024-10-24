from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Type(Enum):
        STATS_NOTIFICATION='stats_notification'
        USAGE_LIMIT='usage_limit'

