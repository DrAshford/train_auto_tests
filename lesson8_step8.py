import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    first_name.send_keys("Lolek")

    last_name = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    last_name.send_keys("Bolek")

    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys("Alokogolek")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file = browser.find_element(By.CSS_SELECTOR, 'input#file')
    file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.location_once_scrolled_into_view
    button.click()


finally:
    time.sleep(5)
    
    browser.quit()