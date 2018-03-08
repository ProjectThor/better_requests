better-requests
---------------

better-requests is a thin wrapper around python's requests library which allows for global defaults.

Simply import ``requests`` from ``better_requests``::

    from better_requests import requests
    requests.get('/foo')

Connection timeout and read timeout for the underlaying ``urllib`` library can be defined by setting
the following environment variables::

    REQUESTS_CONNECTION_TIMEOUT=0.5
    REQUESTS_READ_TIMEOUT=0.5

More fine-grained control for the timeout of the different http verbs is awailable through these 
environment variables::

    REQUESTS_GET_CONNECTION_TIMEOUT
    REQUESTS_GET_READ_TIMEOUT
    REQUESTS_OPTIONS_CONNECTION_TIMEOUT
    REQUESTS_OPTIONS_READ_TIMEOUT
    REQUESTS_HEAD_CONNECTION_TIMEOUT
    REQUESTS_HEAD_READ_TIMEOUT
    REQUESTS_POST_CONNECTION_TIMEOUT
    REQUESTS_POST_READ_TIMEOUT
    REQUESTS_PUT_CONNECTION_TIMEOUT
    REQUESTS_PUT_READ_TIMEOUT
    REQUESTS_PATCH_CONNECTION_TIMEOUT
    REQUESTS_PATCH_READ_TIMEOUT
    REQUESTS_DELETE_CONNECTION_TIMEOUT
    REQUESTS_DELETE_READ_TIMEOUT


Development
-----------

To run all tests use::

    $ python setup.py test


Legal
-----

This software is released under the `MIT License <https://opensource.org/licenses/MIT>`_. 
© 2018 siroop AG, Franco Sebregondi. 
