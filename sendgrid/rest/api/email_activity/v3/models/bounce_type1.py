from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class BounceType1(Enum):
        SOFT='soft'
        HARD='hard'

