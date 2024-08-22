from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

'''TEST'''
try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.XPATH, "//span[contains(@id, 'num1')]")
    num2 = browser.find_element(By.XPATH, "//span[contains(@id, 'num2')]")
    sum = int(num1.text) + int(num2.text)


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum)) # ищем элемент

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()