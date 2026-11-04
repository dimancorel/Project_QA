import pytest
import requests

def get_post():
    response = requests.get(
        "https://example.com/posts/1",
        timeout=10
    )
    response.raise_for_status()
    return response

def fake_get(url, timeout):
    response = requests.Response()
    response.status_code = 500
    response.url = url
    return response

def test_server_error(monkeypatch):
    monkeypatch.setattr(requests,"get", fake_get)
    with pytest.raises(requests.exceptions.HTTPError):
        get_post()