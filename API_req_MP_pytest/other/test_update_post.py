import requests

def test_update_post(api_config):
    url = api_config['base_url']
    timeout_api = api_config['timeout']

    payload = {"id":1, "title": "Updated Title", "body": "Updated Body", "userId":1}
    response = requests.put(f'{url}/posts/1', json=payload, timeout=timeout_api)
    assert response.status_code == 200

    data = response.json()
    assert data['id'] == payload['id']
    assert data['title'] == payload['title']
    assert data['body'] == payload['body']
    assert data['userId'] == payload['userId']