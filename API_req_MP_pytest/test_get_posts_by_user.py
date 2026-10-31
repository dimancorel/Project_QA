import pytest
import requests

@pytest.mark.parametrize('user_id', [1,2,3])
def test_get_posts_by_user(api_config, user_id):
    url = api_config['base_url']
    timeout_api = api_config['timeout']
#Отправить GET-запрос к /posts с параметром userId
    response = requests.get(
        f"{url}/posts",
        params={"userId": user_id},
        timeout=timeout_api
    )
#Проверить HTTP-статус 200
    assert response.status_code == 200
#Преобразовать ответ в Python-объект через .json()
    data = response.json()
#Проверить, что ответ — непустой список
    assert isinstance(data, list) and len(data) > 0
#Проверить, что у каждой публикации значение userId равно user_id.
    for post in data:
        assert post['userId'] == user_id