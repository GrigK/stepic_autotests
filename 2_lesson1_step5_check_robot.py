import math
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/math.html"

    try: 
        browser = webdriver.Chrome()
        browser.get(link)


        x_element = browser.find_element_by_id('input_value')
        x = x_element.text
        y = calc(x)

        people_radio = browser.find_element_by_id("peopleRule")
        people_checked = people_radio.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert people_checked is not None, "People radio is not selected by default"

        input1 = browser.find_element_by_id('answer')
        input1.send_keys(str(y))

        check1 = browser.find_element_by_css_selector('#robotCheckbox')
        check1.click()

        robots_radio = browser.find_element_by_id("robotsRule")
        robots_checked = robots_radio.get_attribute("checked")
        assert robots_checked is None
        robots_radio.click()

        button = browser.find_element_by_css_selector("button.btn")
        button_disabled = button.get_attribute("disabled")
        assert button_disabled is None
        button.click()

        alert=browser.switch_to_alert()
        print (alert.text)

    except Exception as e:
        print(e)

    finally:
        browser.quit()

