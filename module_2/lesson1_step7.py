from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    chest = browser.find_element(By.CSS_SELECTOR, "img").get_attribute("valuex")

    print(chest)

    chest_x = int(chest)

    # x = int(browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text)
    func = list(browser.find_element(By.CSS_SELECTOR, ".form-group span:nth-child(1)").text.split())[2][:-1]

    func = func.replace('x', str(chest_x))
    func = func.replace('ln', 'math.log')
    func = func.replace('sin', 'math.sin')

    result = eval(func, {"math": math, "abs": abs})

    browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(str(result))
    browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']").click()
    browser.find_element(By.CSS_SELECTOR, "button").click()


finally:
    time.sleep(5)
    browser.close()