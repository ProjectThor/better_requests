from doubles import allow
from args_catcher import catch_args

import requests as requests_original
from better_requests import requests
from better_requests.requests import DEFAULT_HEAD_CONNECTION_TIMEOUT, DEFAULT_HEAD_READ_TIMEOUT, \
    DEFAULT_GET_CONNECTION_TIMEOUT, DEFAULT_GET_READ_TIMEOUT, DEFAULT_POST_CONNECTION_TIMEOUT, \
    DEFAULT_POST_READ_TIMEOUT


def head_should_set_a_default_timeout_if_not_provided():
    args_catcher = catch_args(allow(requests_original).head)
    requests.head('/foo')
    assert args_catcher.kwargs['timeout'] == (DEFAULT_HEAD_CONNECTION_TIMEOUT, DEFAULT_HEAD_READ_TIMEOUT)


def head_should_allow_to_override_timeout():
    args_catcher = catch_args(allow(requests_original).head)
    requests.head('/foo', timeout=1.0)
    assert args_catcher.kwargs['timeout'] == 1.0


def get_should_set_a_default_timeout_if_not_provided():
    args_catcher = catch_args(allow(requests_original).get)
    requests.get('/foo')
    assert args_catcher.kwargs['timeout'] == (DEFAULT_GET_CONNECTION_TIMEOUT, DEFAULT_GET_READ_TIMEOUT)


def get_should_allow_to_override_timeout():
    args_catcher = catch_args(allow(requests_original).get)
    requests.get('/foo', timeout=1.0)
    assert args_catcher.kwargs['timeout'] == 1.0


def post_should_set_a_default_timeout_if_not_provided():
    args_catcher = catch_args(allow(requests_original).post)
    requests.post('/foo')
    assert args_catcher.kwargs['timeout'] == (DEFAULT_POST_CONNECTION_TIMEOUT, DEFAULT_POST_READ_TIMEOUT)


def post_should_allow_to_override_timeout():
    args_catcher = catch_args(allow(requests_original).post)
    requests.post('/foo', timeout=1.0)
    assert args_catcher.kwargs['timeout'] == 1.0
