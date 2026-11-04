import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser(request):
    print('starting browser for test...')
    browser = webdriver.Chrome()

    def teardown():
        print('\nclosing browser...')
        browser.quit()

    request.addfinalizer(teardown)
    return browser


class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#login_link')

    def test_guest_should_see_basket_link_on_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
