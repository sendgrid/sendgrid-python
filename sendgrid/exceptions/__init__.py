from typing import Any, Dict


class SendgridException(Exception):
    pass


class ApiException(SendgridException):
    def __init__(self, status_code: int, error: Any, headers: Dict[str, Any] = None):
        self.status_code = status_code
        self.error = error
        self.headers = headers or {}

    def __str__(self):
        return f"ApiException(status_code={self.status_code}, error={self.error}, headers={self.headers})"
