from calc_stepic import calc
from selenium import webdriver

if __name__ == '__main__':

    link = "........"

    try: 
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)


        # x_element = browser.find_element_by_id('input_value')
        # x = x_element.text
        # y = calc(x)

        # input1 = browser.find_element_by_id('answer')
        # input1.send_keys(str(y))

        # check1 = browser.find_element_by_css_selector('#robotCheckbox')
        # check1.click()

        # radio1 = browser.find_element_by_css_selector('#robotsRule')
        # radio1.click()

        # button = browser.find_element_by_css_selector("button.btn")
        # button.click()

        alert=browser.switch_to_alert()
        print (alert.text)

    except Exception as e:
        print(e)

    finally:
        browser.quit()

