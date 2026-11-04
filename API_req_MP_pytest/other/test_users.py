def test_timeout(api_config):
    assert api_config["timeout"]  == 10