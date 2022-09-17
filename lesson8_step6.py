from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    output = browser.find_element(By.CSS_SELECTOR, 'span#input_value')
    text = output.text
    answer = calc(text)

    button = browser.find_element(By.TAG_NAME, 'button')
    checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    radiobutton = browser.find_element(By.CSS_SELECTOR, 'input#robotsRule')
    
    
    input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input.location_once_scrolled_into_view
    input.send_keys(answer)

    checkbox = browser.find_element(By.CSS_SELECTOR, 'input#robotCheckbox')
    checkbox.click()

    
    radiobutton.click();

    button.location_once_scrolled_into_view
    button.click() 

finally:
    time.sleep(10)
    
    browser.quit()
    
    
