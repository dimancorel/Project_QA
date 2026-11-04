import requests


def test_patch_post(api_config):
    api_url = api_config["base_url"]
    api_timeout = api_config["timeout"]

    payload = {"title": "New title"}

    response = requests.patch(
        f"{api_url}/posts/1",
        json=payload,
        timeout=api_timeout
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["id"] == 1