#Для переключения на новую вкладку
#browser.switch_to.window(window_name)

#Чтобы узнать имя новой вкладки
#возвращает массив имён всех вкладок, выбрали вторую:
#new_window = browser.window_handles[1]

#можем запомнить имя текущей вкладки
#first_window = browser.window_handles[0]


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
    button.click()

    print(browser.window_handles)
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    input = browser.find_element(By.ID, "answer")
    x = x_element.text
    input.send_keys(calc(x))
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit_button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла