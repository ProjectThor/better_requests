"""
This module wraps some of the Requests methods and adds default timeouts.
For calls to external services always use the wrapped versions!
"""

import requests
from . import defaults


def get(url, params=None, **kwargs):
    kwargs.setdefault('timeout', (defaults.GET_CONNECTION_TIMEOUT, defaults.GET_READ_TIMEOUT))
    return requests.get(url, params, **kwargs)


def options(url, **kwargs):
    kwargs.setdefault('timeout', (defaults.OPTIONS_CONNECTION_TIMEOUT, defaults.OPTIONS_READ_TIMEOUT))
    return requests.options(url, **kwargs)


def head(url, **kwargs):
    kwargs.setdefault('timeout', (defaults.HEAD_CONNECTION_TIMEOUT, defaults.HEAD_READ_TIMEOUT))
    return requests.head(url, **kwargs)


def post(url, data=None, json=None, **kwargs):
    kwargs.setdefault('timeout', (defaults.POST_CONNECTION_TIMEOUT, defaults.POST_READ_TIMEOUT))
    return requests.post(url, data=data, json=json, **kwargs)


def put(url, data=None, **kwargs):
    kwargs.setdefault('timeout', (defaults.PUT_CONNECTION_TIMEOUT, defaults.PUT_READ_TIMEOUT))
    return requests.put(url, data=data, **kwargs)


def patch(url, data=None, **kwargs):
    kwargs.setdefault('timeout', (defaults.PATCH_CONNECTION_TIMEOUT, defaults.PATCH_READ_TIMEOUT))
    return requests.patch(url, data=data, **kwargs)


def delete(url, **kwargs):
    kwargs.setdefault('timeout', (defaults.DELETE_CONNECTION_TIMEOUT, defaults.DELETE_READ_TIMEOUT))
    return requests.delete(url, **kwargs)
