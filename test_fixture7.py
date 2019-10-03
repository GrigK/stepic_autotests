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

"""
import pytest

languages = ["ru", "de", "ua", "en-gb",]
labels = ["russian", "german", "ukrainian", "english", ]

@pytest.mark.parametrize("code", languages, ids=labels)
def test_guest_should_see_login_link(code):
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
 

Но у него есть подводный камень - из коробки pytest ескейпирует значения ids и если использовать там кириллицу 
или что-то не ascii, то получится фигня. Лечится переопределением pytest_make_parametrize_id в conftest.
"""

"""
еще вариант:

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def dr():
    print("\nstart dr for test..")
    dr = webdriver.Chrome()
    yield dr
    print("\nquit dr..")
    dr.quit()
    
languages = [
    ("ru", "русский"),
    ("de", "немецкий"),
    pytest.param("ua", "украинский",  marks=pytest.mark.xfail(reason="no ua language")),
    ("en-gb", "английский")
]

@pytest.mark.parametrize("code, lang", languages)
def test_guest_should_see_login_link(dr, code, lang): 
    link = "http://selenium1py.pythonanywhere.com/{}/".format(code)
    print("Проверяемый язык %s" % lang)
    dr.get(link)
    dr.find_element_by_css_selector("#login_link")
"""