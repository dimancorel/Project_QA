import pytest
import requests

def test_missing_post_error(api_config):
    api_url = api_config["base_url"]
    api_timeout = api_config["timeout"]
    response = requests.get(f'{api_url}/posts/9999', timeout=api_timeout)
    assert response.status_code == 404
    with pytest.raises(requests.exceptions.HTTPError):
        response.raise_for_status()
