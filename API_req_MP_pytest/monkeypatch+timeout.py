import pytest
import requests


def get_post():
    return requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

def fake_get(url, timeout):
    raise requests.exceptions.Timeout("Server timeout")

def test_get_post_timeout(monkeypatch):
    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(requests.exceptions.Timeout):
        get_post()