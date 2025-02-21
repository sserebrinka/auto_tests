from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a, b = browser.find_element(By.CSS_SELECTOR, "span[id='num1']").text, browser.find_element(By.CSS_SELECTOR, "span[id='num2']").text
    operator = browser.find_element(By.CSS_SELECTOR, "h2 span:nth-child(3)").text

    time.sleep(1)

    select = Select(browser.find_element(By.TAG_NAME, "select"))

    if link == "https://suninjuly.github.io/selects2.html":
        res = int(a) + int(b)
        select.select_by_visible_text(str(res))
    else:
        expression = f"{a} {operator} {b}"
        res = eval(expression)
    
    time.sleep(1)

    select.select_by_visible_text(str(res))
    browser.find_element(By.CSS_SELECTOR, "button").click()
    
finally:
    time.sleep(5)
    browser.close()