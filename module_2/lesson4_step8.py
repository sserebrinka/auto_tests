from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    but = browser.find_element(By.CSS_SELECTOR, "button[id='solve']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", but)

    x = int(browser.find_element(By.CSS_SELECTOR, "span[id='input_value']").text)
    func = list(browser.find_element(By.XPATH, "//label/span[1]").text.split())[2][:-1]

    func = func.replace('x', str(x))
    func = func.replace('ln', 'math.log')
    func = func.replace('sin', 'math.sin')  

    result = eval(func, {"math": math, "abs": abs})

    browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(str(result))

    but.click()
finally:
    time.sleep(5)
    browser.close()