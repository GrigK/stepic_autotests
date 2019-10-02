from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")
# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

browser.find_element_by_id("button")
browser.quit()

