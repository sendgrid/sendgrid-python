from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Accept1(Enum):
        APPLICATION_SLASH_JSON='application/json'
        TEXT_SLASH_CSV='text/csv'

