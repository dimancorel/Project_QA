import requests

def test_delete_post(api_config):
    api_url = api_config["base_url"]
    response = requests.delete(f'{api_url}/posts/1', timeout=10)
    assert response.status_code == 200
    assert response.json() == {}