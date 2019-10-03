# import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select


# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == '__main__':

    link = "http://suninjuly.github.io/selects2.html"

    try: 
        browser = webdriver.Chrome()
        browser.get(link)


        summ = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

        select = Select(browser.find_element_by_id("dropdown"))
        select.select_by_visible_text(str(summ))
        
        browser.find_element_by_css_selector('.btn.btn-default').click()

        alert=browser.switch_to_alert()
        print (alert.text)

    except Exception as e:
        print(e)

    finally:
        browser.quit()

