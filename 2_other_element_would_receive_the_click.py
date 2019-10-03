from selenium import webdriver

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
# проскроллить чтоб элемент появился в области видимости
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# и только потом кликать
button.click()

# пример
# скролл всей страницы вниз на 100px
# browser.execute_script("window.scrollBy(0, 100);")
