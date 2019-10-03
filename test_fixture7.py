"""
запуск теста с разными параметрами с помощью
@pytest.mark.parametrize()
"""
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

"""
Можно задавать параметризацию также для всего тестового класса, чтобы все тесты в классе запустились 
с заданными параметрами. В таком случае отметка о параметризации должна быть перед объявлением класса: 
"""
# @pytest.mark.parametrize('language', ["ru", "en-gb"])
# class TestLogin(object):
#     def test_guest_should_see_login_link(self, browser, language):
#         link = f"http://selenium1py.pythonanywhere.com/{language}/"
#         browser.get(link)
#         browser.find_element_by_css_selector("#login_link")
#         # этот тест запустится 2 раза
#
#     def test_guest_should_see_navbar_element(self, browser, language):
#         # этот тест тоже запустится дважды
#         pass

"""
Например, это может выглядеть вот так:

languages = [
    ("ru", "русский"),
    ("de" "немецкий"),
    ("ua", "украинский"),
    ("en-gb", "английский")
]

@pytest.mark.parametrize("code, lang", languages)
def test_guest_should_see_login_link(browser, code, lang) 
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    print("Проверяемый язык %s" % lang)
"""