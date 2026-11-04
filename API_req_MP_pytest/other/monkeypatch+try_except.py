import pytest
import requests


def get_post_safely():
    try:
        return requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=10
        )
    except requests.exceptions.Timeout:
        return None

def fake_get(url, timeout):
    raise requests.exceptions.Timeout("Server timeout")

def test_get_post_timeout_handled(monkeypatch):
    monkeypatch.setattr(requests, "get", fake_get)
    result = get_post_safely()
    assert result is None