import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/2/1.html')
    time.sleep(1)
    
    for i, url in enumerate([
        'http://parsinger.ru/blank/2/2.html',
        'http://parsinger.ru/blank/2/3.html',
        'http://parsinger.ru/blank/2/4.html'
    ], start=1):
        browser.execute_script(f'window.open("{url}", "_blank{i}");')
        time.sleep(1)  

    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        for y in browser.find_elements(By.CLASS_NAME, 'check'):
            y.click()