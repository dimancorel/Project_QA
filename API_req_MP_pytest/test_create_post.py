import requests

def test_create_post(api_config):
    base_url = api_config["base_url"]
    timeout_conf = api_config["timeout"]

    payload = {
        "title": "My first autotest",
        "body": "Learning Python requests",
        "userId": 1
    }

    #Отправляем POST и получаем HTTP-ответ (Response)
    response = requests.post(
        f"{base_url}/posts",
        json=payload,
        timeout=timeout_conf
    )
    #Уже пришёл Response
    assert response.status_code == 201
    #Преобразуем JSON из ответа сервера в Python-словарь.
    data = response.json()

    print(data)
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
