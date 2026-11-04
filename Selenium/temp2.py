from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.implicitly_wait(20)

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
money = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.ID, "input_value")
input = browser.find_element(By.ID, "answer")
x = x_element.text
input.send_keys(calc(x))
submit_button = browser.find_element(By.ID, "solve")
submit_button.click()

time.sleep(10)