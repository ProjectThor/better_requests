"""
This module wraps some of the Requests methods and adds default timeouts.
For calls to external services always use the wrapped versions!
"""

import requests
from os import environ


def _float_env(key, default):
    value = environ.get(key, default)
    return float(value) if value else None


DEFAULT_CONNECTION_TIMEOUT = _float_env('REQUESTS_CONNECTION_TIMEOUT', 0.5)
DEFAULT_READ_TIMEOUT = _float_env('REQUESTS_READ_TIMEOUT', None)
DEFAULT_HEAD_CONNECTION_TIMEOUT = _float_env('REQUESTS_HEAD_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
DEFAULT_HEAD_READ_TIMEOUT = _float_env('REQUESTS_HEAD_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
DEFAULT_GET_CONNECTION_TIMEOUT = _float_env('REQUESTS_GET_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
DEFAULT_GET_READ_TIMEOUT = _float_env('REQUESTS_GET_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
DEFAULT_POST_CONNECTION_TIMEOUT = _float_env('REQUESTS_POST_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
DEFAULT_POST_READ_TIMEOUT = _float_env('REQUESTS_POST_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)


def head(url, **kwargs):
    kwargs.setdefault('timeout', (DEFAULT_HEAD_CONNECTION_TIMEOUT, DEFAULT_HEAD_READ_TIMEOUT))
    return requests.head(url, **kwargs)


def get(url, params=None, **kwargs):
    kwargs.setdefault('timeout', (DEFAULT_GET_CONNECTION_TIMEOUT, DEFAULT_GET_READ_TIMEOUT))
    return requests.get(url, params, **kwargs)


def post(url, data=None, json=None, **kwargs):
    kwargs.setdefault('timeout', (DEFAULT_POST_CONNECTION_TIMEOUT, DEFAULT_POST_READ_TIMEOUT))
    return requests.post(url, data=data, json=json, **kwargs)
