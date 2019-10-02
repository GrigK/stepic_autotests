from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from calc_stepic import calc


if __name__ == '__main__':

    link = "http://suninjuly.github.io/explicit_wait2.html"

    try: 
        browser = webdriver.Chrome()
        # browser.implicitly_wait(5)
        browser.get(link)

        button = browser.find_element_by_css_selector("button.btn")
        # ждем нужную цену в $100
        WebDriverWait(browser, 12).until(
                EC.text_to_be_present_in_element((By.ID, "price"), "100")
            )
        button.click()

        # потом решаем задачку и получаем ответ
        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = calc(x)

        input1 = browser.find_element_by_id('answer')
        input1.send_keys(str(y))

        btn = browser.find_element_by_id('solve')
        btn.click()

        alert=browser.switch_to_alert()
        print (alert.text)

    except Exception as e:
        print(e)

    finally:
        browser.quit()

