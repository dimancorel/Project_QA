import requests

def test_get_post_json(api_config):
    api_url = api_config["base_url"]
    api_timeout = api_config["timeout"]
    response = requests.get(f'{api_url}/posts/1', timeout=api_timeout)

    assert response.status_code == 200
    # Проверить тип объекта
    assert isinstance(data, dict)
    data = response.json()
    assert data["id"] == 1

    # Проверить, что значение — строка и что строка непустая
    assert isinstance(data["title"], str) and len(data["title"]) > 0
    assert isinstance(data["body"], str) and len(data["body"]) > 0