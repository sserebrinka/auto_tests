from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input[name='firstname']").send_keys('lena')
    browser.find_element(By.CSS_SELECTOR, "input[name='lastname']").send_keys('ignateva')
    browser.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys('abc@gmail.com')

    browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button").click()
finally:
    time.sleep(5)
    browser.close()