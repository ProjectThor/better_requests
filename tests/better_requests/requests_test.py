import pytest
from args_catcher import catch_args
from doubles import allow
import requests as requests_original

from better_requests import requests, defaults

HTTP_METHODS = ['get', 'options', 'head', 'post', 'put', 'patch', 'delete']

@pytest.mark.parametrize("http_method", HTTP_METHODS)
def should_set_a_default_timeout_if_not_provided(http_method):
    args_catcher = catch_args(getattr(allow(requests_original), http_method))
    getattr(requests, http_method)('/foo')
    assert args_catcher.kwargs['timeout'] == (
        defaults.__dict__[f'{http_method.upper()}_CONNECTION_TIMEOUT'],
        defaults.__dict__[f'{http_method.upper()}_READ_TIMEOUT']
    )


@pytest.mark.parametrize("http_method", HTTP_METHODS)
def should_allow_to_override_timeout_by_argument(http_method):
    args_catcher = catch_args(getattr(allow(requests_original), http_method))
    getattr(requests, http_method)('/foo', timeout=1.0)
    assert args_catcher.kwargs['timeout'] == 1.0
