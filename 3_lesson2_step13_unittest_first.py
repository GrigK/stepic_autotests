from typing import Any

import unittest
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    data_inputs = ['Vasya', 'Pupkin', 'pupkin.team@gmail.com']
    all_css_inputs = ['.first_block .first', '.first_block .second', '.first_block .third']
    fields_input = list(zip(data_inputs, all_css_inputs))
    pattern_text = "Congratulations! You have successfully registered!"

    def test_first(self):
        self.observer_site(self.link1)

    def test_second(self):
        self.observer_site(self.link2)

    def observer_site(self, link):
        browser = webdriver.Chrome()
        browser.implicitly_wait(2)
        browser.get(link)

        for data_input, css_input in self.fields_input:
            browser.find_element_by_css_selector(css_input).send_keys(data_input)
            # input_field = browser.find_element_by_css_selector(css_input)
            # input_field.send_keys(data_input)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text: str = welcome_text_elt.text

        # с помощью unittest проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(self.pattern_text, welcome_text)

        browser.quit()


if __name__ == '__main__':
    unittest.main()
