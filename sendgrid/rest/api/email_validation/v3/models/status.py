from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum



class Status(Enum):
        INITIATED='Initiated'
        QUEUED='Queued'
        READY='Ready'
        PROCESSING='Processing'
        DONE='Done'
        ERROR='Error'

