from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    #people_radio = browser.find_element(By.ID, "peopleRule")
    #people_checked = people_radio.get_attribute("checked")
    #print("value of people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"
    #assert people_checked == "true", "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit(

    < input


    #class ="form-check-input" type="radio" name="ruler" id="peopleRule" value="people" checked >

    #people_radio = browser.find_element_by_id("peopleRule")

    #print(people_radio.get_attribute("name"))
    # Напечатает ruler, т.е. текстовое значение аттрибута

    #print(people_radio.get_attribute("checked"))
    # Напечатает true, т.е. факт того что аттрибут существует. Учтите что true это в данном случае строка, а не булево значение.

    #print(people_radio.get_attribute("href"))
    # Напечатает None, т.к. аттрибут не существует. И это не строка а None-значение.