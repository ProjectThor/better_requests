from os import environ


def _float_env(key, default):
    value = environ.get(key, default)
    return float(value) if value else None


DEFAULT_CONNECTION_TIMEOUT = _float_env('REQUESTS_CONNECTION_TIMEOUT', 0.5)
DEFAULT_READ_TIMEOUT = _float_env('REQUESTS_READ_TIMEOUT', None)
GET_CONNECTION_TIMEOUT = _float_env('REQUESTS_GET_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
GET_READ_TIMEOUT = _float_env('REQUESTS_GET_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
OPTIONS_CONNECTION_TIMEOUT = _float_env('REQUESTS_OPTIONS_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
OPTIONS_READ_TIMEOUT = _float_env('REQUESTS_OPTIONS_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
HEAD_CONNECTION_TIMEOUT = _float_env('REQUESTS_HEAD_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
HEAD_READ_TIMEOUT = _float_env('REQUESTS_HEAD_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
POST_CONNECTION_TIMEOUT = _float_env('REQUESTS_POST_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
POST_READ_TIMEOUT = _float_env('REQUESTS_POST_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
PUT_CONNECTION_TIMEOUT = _float_env('REQUESTS_PUT_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
PUT_READ_TIMEOUT = _float_env('REQUESTS_PUT_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
PATCH_CONNECTION_TIMEOUT = _float_env('REQUESTS_PATCH_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
PATCH_READ_TIMEOUT = _float_env('REQUESTS_PATCH_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
DELETE_CONNECTION_TIMEOUT = _float_env('REQUESTS_DELETE_CONNECTION_TIMEOUT', DEFAULT_CONNECTION_TIMEOUT)
DELETE_READ_TIMEOUT = _float_env('REQUESTS_DELETE_READ_TIMEOUT', DEFAULT_READ_TIMEOUT)
