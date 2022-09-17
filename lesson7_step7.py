from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    output = browser.find_element(By.TAG_NAME, 'img')
    text = output.get_attribute("valuex")
    answer = calc(text)

    input = browser.find_element(By.CSS_SELECTOR, "div.form-group input")
    input.send_keys(answer)

    checkbox = browser.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]')
    checkbox.click()

    radiobutton = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    radiobutton.click();

    time.sleep(3)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click() 

finally:
    time.sleep(10)
    
    browser.quit()
    
    
