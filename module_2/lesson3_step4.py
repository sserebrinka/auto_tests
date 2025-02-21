from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os, math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, ".container button").click()
    browser.switch_to.alert.accept()

    x = int(browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text)
    func = list(browser.find_element(By.XPATH, "//label/span[1]").text.split())[2][:-1]

    time.sleep(1)

    func = func.replace('x', str(x))
    func = func.replace('ln', 'math.log')
    func = func.replace('sin', 'math.sin')   

    result = eval(func, {"math": math, "abs": abs})

    time.sleep(1)

    browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(str(result))
    browser.find_element(By.CSS_SELECTOR, "button").click()
finally:
    time.sleep(5)
    browser.close()