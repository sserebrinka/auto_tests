import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR, "button").click()

    new_win = browser.window_handles[1]
    browser.switch_to.window(new_win)

    x = int(browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text)
    func = list(browser.find_element(By.XPATH, "//label/span[1]").text.split())[2][:-1]

    func = func.replace('x', str(x))
    func = func.replace('ln', 'math.log')
    func = func.replace('sin', 'math.sin')  

    result = eval(func, {"math": math, "abs": abs})

    browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(str(result))
    browser.find_element(By.CSS_SELECTOR, "button").click()
finally:
    time.sleep(5)
    browser.close()