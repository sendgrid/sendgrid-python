from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class IdentifierType1(Enum):
        EMAIL='email'
        PHONE_NUMBER_ID='phone_number_id'
        EXTERNAL_ID='external_id'
        ANONYMOUS_ID='anonymous_id'

