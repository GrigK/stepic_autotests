from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

'''
Если мы хотим в тесте кликнуть на кнопку, а она в этот момент неактивна, 
то WebDriver все равно проэмулирует действие нажатия на кнопку, но данные 
не будут отправлены.
'''