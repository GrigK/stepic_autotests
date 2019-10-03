import math
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    link = "http://suninjuly.github.io/get_attribute.html"

    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        sunduk = browser.find_element_by_id('treasure')
        newValue = calc(sunduk.get_attribute("valuex"))

        input1 = browser.find_element_by_id('answer')
        input1.send_keys(str(newValue))

        for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
            browser.find_element_by_css_selector(selector).click()

        alert=browser.switch_to_alert()
        print (alert.text)

    except Exception as e:
        print(e)

    finally:
        browser.quit()

