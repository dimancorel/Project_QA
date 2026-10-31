import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, 'input[name=firstname]')
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, 'input[name=lastname]')
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, 'input[name=email]')
    input3.send_keys("test@example.com")

    option1 = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    print(option1)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'temp.py')  # добавляем к этому пути имя файла
    print(os.path.abspath(os.path.dirname(__file__)))
    option1.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(35)
    # закрываем браузер после всех манипуляций
    browser.quit()