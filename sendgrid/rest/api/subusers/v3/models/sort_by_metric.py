from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class SortByMetric(Enum):
        BLOCKS='blocks'
        BOUNCES='bounces'
        CLICKS='clicks'
        DELIVERED='delivered'
        OPENS='opens'
        REQUESTS='requests'
        UNIQUE_CLICKS='unique_clicks'
        UNIQUE_OPENS='unique_opens'
        UNSUBSCRIBES='unsubscribes'

