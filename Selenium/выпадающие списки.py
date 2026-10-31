from selenium.webdriver.support.ui import Select
#select = Select(browser.find_element(By.TAG_NAME, "select"))
#а уже потом:
# select.select_by_value("1") # ищем элемент с текстом "Python"
# select.select_by_visible_text("text")  по видимому тексту
# select.select_by_index(index) по его индексу или порядковому номеру


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")
    z = int(x.text) + int(y.text)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(z))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(35)
    # закрываем браузер после всех манипуляций
    browser.quit()