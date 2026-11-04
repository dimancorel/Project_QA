import pytest
import requests


@pytest.mark.parametrize("post_id,expected_status",
                         [(1,200),
                          (9999,404)])

def test_get_post_status(api_config, post_id, expected_status):
    # Получи base_url и timeout
    url = api_config['base_url']
    timeout_api = api_config['timeout']
    # Отправь GET-запрос
    response = requests.get(f'{url}/posts/{post_id}', timeout = timeout_api)
    assert response.status_code == expected_status

404 — статус HTTP-ответа.
HTTPError — исключение Python, которое можно вызвать через raise_for_status().
FAILED — результат теста, если проверка не соответствует ожиданиям.