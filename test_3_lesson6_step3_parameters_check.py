import math
import time
import pytest
from selenium import webdriver

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]

total_answer = ''


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

    print()
    print("=====================")
    print(total_answer)


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    global total_answer
    answer = math.log(int(time.time()))

    browser.get(link)
    txt_area = browser.find_element_by_css_selector(".textarea.ember-text-area.ember-view")
    txt_area.send_keys(str(answer))

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    pre = browser.find_element_by_css_selector("pre.smart-hints__hint")
    pre_text = pre.text
    if "Correct!" not in pre_text:
        total_answer = f'{total_answer}{pre_text}'
    assert "Correct!" in pre_text
