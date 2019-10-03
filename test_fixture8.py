"""
Чтобы запустить тест с нужной маркировкой, нужно передать в командной строке параметр -m и нужную метку:
pytest -s -v -m smoke test_fixture8.py

You can register custom marks in your pytest.ini file like this:
[pytest]
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    serial

Note that everything after the : is an optional description.

Так же можно маркировать целый тестовый класс. В этом случае маркировка
будет применена ко всем тестовым методам, входящим в класс
"""
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")