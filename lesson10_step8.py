from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, 'price'),'$100'))
    book = browser.find_element(By.ID, "book")
    book.click()

    submit = browser.find_element(By.ID, 'solve')
    submit.location_once_scrolled_into_view
    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(answer)
    submit.click()

    alert = browser.switch_to.alert
    message = alert.text
    code = message.split(': ')[-1]
    print(code)

finally:
    time.sleep(3)

    browser.quit()
