import os

import pytest


@pytest.fixture
def clean_environ(request):
    envvars = ("EXTRA_VERIFY_CERTS", "REQUESTS_CA_BUNDLE")

    def reset():
        for envvar in envvars:
            if envvar not in os.environ:
                continue
            del os.environ[envvar]

    reset()
    yield os.environ
    reset()
