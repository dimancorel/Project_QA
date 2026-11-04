import pytest

@pytest.fixture(scope="session")
def api_config():
    return {
        "base_url": "https://jsonplaceholder.typicode.com",
        "timeout": 10
    }