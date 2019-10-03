import os
from selenium import webdriver


data_inputs = ['Vasya', 'Pupkin', 'pupkin.team@gmail.com']
names_input = ['firstname', 'lastname', 'email']
fields_input = list(zip(data_inputs, names_input))

if __name__ == '__main__':

    link = "http://suninjuly.github.io/file_input.html"

    try: 
        browser = webdriver.Chrome()
        browser.get(link)

        for data_input, name_input in fields_input:
            # input_field = browser.find_element_by_css_selector(f'input[name="{name_input}"]')
            input_field = browser.find_element_by_name(name_input)
            input_field.send_keys(data_input)

        current_dir = os.path.abspath(os.path.dirname('__file__'))
        file_path = os.path.join(current_dir, '_readme_.txt')
        file_field = browser.find_element_by_id('file')
        file_field.send_keys(file_path)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        alert=browser.switch_to_alert()
        print (alert.text)
        alert.accept()

    except Exception as e:
        print(e)

    finally:
        browser.quit()

