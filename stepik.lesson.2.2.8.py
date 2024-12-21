from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = " http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Andrey")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Khmelnov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("aaa")
    file_button = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname("/Users/holly/Library/Mobile Documents/com~apple~TextEdit/Documents/aaa.txt"))
    file_path = os.path.join(current_dir, "aaa.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
