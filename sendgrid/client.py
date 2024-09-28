from typing import List, Optional
from sendgrid.http.http_client import SendgridHttpClient, HttpClient
from sendgrid.http.request import Request
from sendgrid.base.url_builder import build_url

# class AuthStrategy:
#     def authenticate(self):
#         pass
#
#
# class ApiKeyAuthStrategy(AuthStrategy):
#     def __init__(self, api_key):
#         self.api_key = api_key
#
#     def authenticate(
#             self,
#             headers: Optional[Dict[str, str]] = None
#     ):
#         headers["Authorization"] = f"Bearer {self.api_key}"
#


class Client:
    def __init__(
        self,
        api_key: str,
        region: Optional[str] = None,
        edge: Optional[str] = None,
        http_client: Optional[HttpClient] = None,
        user_agent_extensions: Optional[List[str]] = None,
    ):
        self.api_key = api_key
        self.region = region
        self.edge = edge
        self.user_agent_extensions = user_agent_extensions or []
        self.http_client: SendgridHttpClient = SendgridHttpClient()

    def send(self, request: Request):
        url = build_url(request.url, self.region)
        response = self.http_client.request(
            method=request.method,
            url=url,
            data=request.data,
            headers=request.headers,
            api_key=self.api_key,
        )
        return response