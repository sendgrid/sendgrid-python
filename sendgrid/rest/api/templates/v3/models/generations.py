from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Generations(Enum):
        LEGACY='legacy'
        DYNAMIC='dynamic'
        LEGACY_COMMA_DYNAMIC='legacy,dynamic'

