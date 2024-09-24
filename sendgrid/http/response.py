from typing import Any, Optional


class HTTPStatus:
    SUCCESS = range(200, 300)  # Success codes: 200-299
    CLIENT_ERROR = range(400, 500)  # Client error codes: 400-499
    SERVER_ERROR = range(500, 600)  # Server error codes: 500-599


class Response(object):
    def __init__(
            self,
            status_code: int,
            text: str,
            headers: Optional[Any] = None,
    ):
        self.content = text
        self.headers = headers
        self.cached = False
        self.status_code = status_code
        self.ok = self.status_code < 400

    @property
    def text(self) -> str:
        return self.content

    def is_success(self):
        return self.status_code in HTTPStatus.SUCCESS

    def __repr__(self) -> str:
        return "HTTP {} {}".format(self.status_code, self.content)