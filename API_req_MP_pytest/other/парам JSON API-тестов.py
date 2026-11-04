import pytest
import requests

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_posts_json(api_config, post_id):
    url = api_config['base_url']
    timeout_api = api_config['timeout']
    response = requests.get(f'{url}/posts/{post_id}', timeout = timeout_api)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data['id'] == post_id
    assert isinstance(data["title"], str) and len(data["title"]) > 0
    assert isinstance(data["body"], str) and len(data["body"]) > 0