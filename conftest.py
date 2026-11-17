import pytest
from utils.auth import get_token


@pytest.fixture(scope="session")
def token():
    return get_token()


@pytest.fixture(scope="session")
def auth_headers(token):
    return {"Authorization": f"Bearer {token}"}