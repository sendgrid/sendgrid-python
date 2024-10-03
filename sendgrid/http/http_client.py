import logging
import os
from logging import Logger
from typing import Any, Dict, Optional, Tuple
from urllib.parse import urlencode

from requests import Request, Session, hooks
from requests.adapters import HTTPAdapter

from sendgrid.exceptions import SendgridException
from sendgrid.http.response import Response

_logger = logging.getLogger("sendgrid.http_client")  # TODO: Validate this logger


class HttpClient:
    def __init__(self, logger: Logger, is_async: bool, timeout: Optional[float] = None):
        self.logger = logger
        self.is_async = is_async

        if timeout is not None and timeout <= 0:
            raise ValueError(timeout)
        self.timeout = timeout

        self._test_only_last_request: Optional[Request] = None
        self._test_only_last_response: Optional[Response] = None

    """
    An abstract class representing an HTTP client.
    """

    def request(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Response:
        """
        Make an HTTP request.
        """
        raise SendgridException("HttpClient is an abstract class")

    def log_request(self, kwargs: Dict[str, Any]) -> None:
        """
        Logs the HTTP request
        """
        self.logger.info("-- BEGIN Twilio API Request --")

        if kwargs["params"]:
            self.logger.info(
                "{} Request: {}?{}".format(
                    kwargs["method"], kwargs["url"], urlencode(kwargs["params"])
                )
            )
            self.logger.info("Query Params: {}".format(kwargs["params"]))
        else:
            self.logger.info("{} Request: {}".format(kwargs["method"], kwargs["url"]))

        if kwargs["headers"]:
            self.logger.info("Headers:")
            for key, value in kwargs["headers"].items():
                # Do not log authorization headers
                if "authorization" not in key.lower():
                    self.logger.info("{} : {}".format(key, value))

        self.logger.info("-- END Twilio API Request --")

    def log_response(self, status_code: int, response: Response) -> None:
        """
        Logs the HTTP response
        """
        self.logger.info("Response Status Code: {}".format(status_code))
        self.logger.info("Response Headers: {}".format(response.headers))


class AsyncHttpClient(HttpClient):
    """
    An abstract class representing an asynchronous HTTP client.
    """

    async def request(
        self,
        method: str,
        uri: str,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth: Optional[Tuple[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Response:
        """
        Make an asynchronous HTTP request.
        """
        raise SendgridException("AsyncHttpClient is an abstract class")


class SendgridHttpClient(HttpClient):
    """
    General purpose HTTP Client for interacting with the Twilio API
    """

    def __init__(
        self,
        pool_connections: bool = True,
        request_hooks: Optional[Dict[str, object]] = None,
        timeout: Optional[float] = None,
        logger: logging.Logger = _logger,
        proxy: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
    ):
        """
        Constructor for the TwilioHttpClient
        :param pool_connections
        :param request_hooks
        :param timeout: Timeout for the requests.
                    Timeout should never be zero (0) or less
        :param logger
        :param proxy: Http proxy for the requests session
        :param max_retries: Maximum number of retries each request should attempt
        """
        super().__init__(logger, False, timeout)
        self.session = Session() if pool_connections else None
        if self.session and max_retries is not None:
            self.session.mount("https://", HTTPAdapter(max_retries=max_retries))
        if self.session is not None:
            self.session.mount(
                "https://", HTTPAdapter(pool_maxsize=min(32, os.cpu_count() + 4))
            )
        self.request_hooks = request_hooks or hooks.default_hooks()
        self.proxy = proxy if proxy else {}

    def request(
        self,
        method: str,
        url: str,
        api_key: str = None,
        params: Optional[Dict[str, object]] = None,
        data: Optional[Dict[str, object]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
        allow_redirects: bool = False,
    ) -> Response:
        """
        Make an HTTP Request with parameters provided.

        :param api_key:
        :param method: The HTTP method to use
        :param url: The URL to request
        :param params: Query parameters to append to the URL
        :param data: Parameters to go in the body of the HTTP request
        :param headers: HTTP Headers to send with the request
        :param timeout: Socket/Read timeout for the request
        :param allow_redirects: Whether to allow redirects
        See the requests documentation for explanation of all these parameters

        :return: An HTTP response
        """
        if timeout is None:
            timeout = self.timeout
        elif timeout <= 0:
            raise ValueError(timeout)

        headers["Authorization"] = f"Bearer {api_key}"
        # Currently supporting 'application/json' content type
        headers["Content-Type"] = "application/json"
        # auth.authenticate()
        kwargs = {
            "method": method.upper(),
            "url": url,
            "params": params,
            "headers": headers,
            "hooks": self.request_hooks,
        }
        if headers and headers.get("Content-Type") == "application/json":
            kwargs["json"] = data
        else:
            kwargs["data"] = data
        self.log_request(kwargs)

        self._test_only_last_response = None
        session = self.session or Session()
        request = Request(**kwargs)
        self._test_only_last_request = Request(**kwargs)

        prepped_request = session.prepare_request(request)

        settings = session.merge_environment_settings(
            prepped_request.url, self.proxy, None, None, None
        )

        response = session.send(
            prepped_request,
            allow_redirects=allow_redirects,
            timeout=timeout,
            **settings,
        )
        print(response)
        print(response.status_code)
        print(response.headers)
        self.log_response(response.status_code, response)

        self._test_only_last_response = Response(
            int(response.status_code), response.text, response.headers
        )

        return self._test_only_last_response
