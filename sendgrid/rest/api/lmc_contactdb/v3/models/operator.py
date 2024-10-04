from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Operator(Enum):
        EQ='eq'
        NE='ne'
        LT='lt'
        GT='gt'
        CONTAINS='contains'

