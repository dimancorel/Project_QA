def test_api_url(api_config):
    assert api_config["base_url"].startswith("https://")