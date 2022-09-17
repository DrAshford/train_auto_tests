import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.CSS_SELECTOR, '#num1').text
    second = browser.find_element(By.CSS_SELECTOR, '#num2').text
    
    selector = browser.find_element(By.TAG_NAME, 'select').click()
    answer = browser.find_element(By.CSS_SELECTOR, f'option[value="{int(first)+int(second)}"]')
    answer.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(5)

    browser.quit()
