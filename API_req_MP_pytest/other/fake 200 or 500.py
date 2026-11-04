import pytest
import requests


def get_post():
    response = requests.get(
        "https://example.com/posts/1",
        timeout=10
    )
    response.raise_for_status()
    return response

@pytest.mark.parametrize("status_code, should_raise", [
    (200, False),
    (500, True)
])
def test_get_post_status(monkeypatch, status_code, should_raise):

    def fake_get(url, timeout):
        response = requests.Response()
        response.status_code = status_code
        response.url = url
        return response

    monkeypatch.setattr(requests, "get", fake_get)
    if should_raise:
        with pytest.raises(requests.exceptions.HTTPError):
            get_post()
    else:
        result = get_post()
        assert result.status_code == status_code