from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class UserType1(Enum):
        ADMIN='admin'
        OWNER='owner'
        TEAMMATE='teammate'
