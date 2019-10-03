from calc_stepic import calc
from selenium import webdriver

if __name__ == '__main__':

    link = "http://suninjuly.github.io/redirect_accept.html"

    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        button = browser.find_element_by_css_selector("button.trollface.btn.btn-primary")
        button.click()

        current_window = browser.current_window_handle
        windows = browser.window_handles

        assert len(windows) == 2

        new_window = windows[1] if windows[1] != current_window else windows[0]
        browser.switch_to.window(new_window)

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

