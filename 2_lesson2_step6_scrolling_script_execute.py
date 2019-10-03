import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/execute_script.html"

    try: 
        browser = webdriver.Chrome()
        browser.get(link)


        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = calc(x)

        input1 = browser.find_element_by_id('answer')
        browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
        input1.send_keys(str(y))

        button = browser.find_element_by_css_selector("button.btn")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)

        check1 = browser.find_element_by_css_selector('#robotCheckbox')
        check1.click()

        radio1 = browser.find_element_by_css_selector('#robotsRule')
        radio1.click()

        button.click()

        alert=browser.switch_to_alert()
        print (alert.text)

    except Exception as e:
        print(e)

    finally:
        browser.quit()

