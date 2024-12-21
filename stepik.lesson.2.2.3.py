import math


def calc(x):
    return sum(z, y)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    z_element = browser.find_element(By.ID, "num1")
    z = z_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    x = int(z) + int(y)
    browser.find_element(By.ID, "dropdown").click()
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(x))
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
