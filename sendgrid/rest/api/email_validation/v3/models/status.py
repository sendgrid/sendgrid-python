from enum import Enum
from enum import Enum


class Status(Enum):
    INITIATED = "Initiated"
    QUEUED = "Queued"
    READY = "Ready"
    PROCESSING = "Processing"
    DONE = "Done"
    ERROR = "Error"
