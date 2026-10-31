import requests

def test_get_post_headers_and_structure(api_config):
    url = api_config['base_url']
    timeout_api = api_config['timeout']

    response = requests.get(
        f"{url}/posts/1",
        timeout=timeout_api
    )
#Проверить HTTP-статус 200
    assert response.status_code == 200

# получить значение заголовка с названием "Content-Type"
# "" — вернуть пустую строку, если такого заголовка нет.
# content_type — переменная, в которую сохраняем найденное значение.
    content_type = response.headers.get("Content-Type", "")
    # Проверить наличие подстроки
    assert "application/json" in content_type.lower()

#Преобразовать ответ в Python-объект через .json()
    data = response.json()
#Проверить, что ответ — непустой словарь
    assert isinstance(data, dict) and len(data) > 0
    # Проверить наличие ключа
    assert "id" in data
    assert "userId" in data
    assert "title" in data
    assert "body" in data
    assert data["id"] == 1
    assert len(data["title"]) > 0
    assert len(data["body"]) > 0



