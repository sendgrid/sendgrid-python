import warnings

import asyncio
from urllib.error import HTTPError, URLError

import aiohttp
from sendgrid import SendGridClientError, SendGridServerError, SendGridClient

from sendgrid.client import SendGridAPIClient


class AsyncSendGridClient(SendGridClient):
    @asyncio.coroutine
    def _make_request(self, message):
        connector = aiohttp.TCPConnector(conn_timeout=self.timeout)
        if self.proxies:
            if 'http' in self.proxies:
                connector = aiohttp.ProxyConnector(proxy=self.proxies['http'], conn_timeout=self.timeout)
            else:
                warnings.warn("Only http proxies are supported for async connections")
        session = aiohttp.ClientSession(connector=connector)
        headers = {
            'User-Agent': self.useragent,
            'Accept': '*/*',
        }
        if self.username is None:
            # Using API key
            headers['Authorization'] = 'Bearer {}'.format(self.password)
        data = self._build_body(message)
        method = 'POST' if data else 'GET'
        try:
            resp = yield from session.request(method, self.mail_url, data=data, headers=headers)
        except aiohttp.ClientTimeoutError:
            session.close()
            raise URLError('Request timeout')
        resp_body = yield from resp.text()
        session.close()
        if resp.status == 200:
            return resp.status, resp_body
        elif 400 <= resp.status < 600:
            raise HTTPError(resp.status, resp_body, None, None, None)
        else:
            assert False


class AsyncSendGridAPIClient(SendGridAPIClient):
    @asyncio.coroutine
    def _build_request(self, url, json_header=False, method='GET', data=None):
        connector = aiohttp.TCPConnector(conn_timeout=self.timeout)
        if self.proxies:
            if 'http' in self.proxies:
                connector = aiohttp.ProxyConnector(proxy=self.proxies['http'], conn_timeout=self.timeout)
            else:
                warnings.warn("Only http proxies are supported for async connections")
        session = aiohttp.ClientSession(connector=connector)
        headers = {
            'User-Agent': self.useragent,
            'Authorization': 'Bearer {}'.format(self.apikey)
        }
        if json_header:
            headers['Content-Type'] = 'application/json'
        try:
            resp = yield from session.request(method, url, data=data, headers=headers)
        except aiohttp.ClientTimeoutError:
            session.close()
            raise SendGridClientError(408, 'Request timeout')
        resp_body = yield from resp.text()
        session.close()
        if resp.status == 200:
            return resp.status, resp_body
        elif 400 <= resp.status < 500:
            raise SendGridClientError(resp.status, resp_body)
        elif 500 <= resp.status < 600:
            raise SendGridServerError(resp.status, resp_body)
        else:
            assert False
