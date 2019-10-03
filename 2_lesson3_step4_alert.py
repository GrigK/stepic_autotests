import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/alert_accept.html"

    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        # первая страница
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        alert=browser.switch_to_alert()
        alert.accept()

        # вторая страница
        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = calc(x)

        input1 = browser.find_element_by_id('answer')
        input1.send_keys(str(y))

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        alert=browser.switch_to_alert()
        print (alert.text)

    except Exception as e:
        print(e)

    finally:
        browser.quit()

