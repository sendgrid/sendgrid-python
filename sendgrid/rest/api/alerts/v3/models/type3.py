from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Type3(Enum):
        USAGE_LIMIT='usage_limit'
        STATS_NOTIFICATION='stats_notification'

