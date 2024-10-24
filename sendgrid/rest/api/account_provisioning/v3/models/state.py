from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class State(Enum):
        ACTIVATED='activated'
        DEACTIVATED='deactivated'
        SUSPENDED='suspended'
        BANNED='banned'
        INDETERMINATE='indeterminate'

