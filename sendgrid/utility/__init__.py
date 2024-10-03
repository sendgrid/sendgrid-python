import json
from typing import Any

from sendgrid.http.response import Response


def parse_response(self, response: Response) -> Any:

    if response.status_code < 200 or response.status_code >= 300:
        raise self.exception(response, "Unable to create record")

    return json.loads(response.text)
