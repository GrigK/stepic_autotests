from selenium import webdriver
import time

try:
    link = "https://stepik.org/catalog?auth=login"
    browser = webdriver.Chrome()
    browser.get(link)

    # TODO: переделать sleep
    time.sleep(3) # плохая практика
    mail_l = browser.find_element_by_id("id_login_email")
    mail_l.send_keys("x@x.ru")

    pass_l = browser.find_element_by_id("id_login_password")
    pass_l.send_keys("pass123")

    # button = browser.find_element_by_xpath('//button[text()="Войти"]')
    button = browser.find_element_by_css_selector('button.sign-form__btn.button_with-loader')
    button.click()

finally:
    time.sleep(15)
    browser.quit()
