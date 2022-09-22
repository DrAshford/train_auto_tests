import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

parameters =    ['https://stepik.org/lesson/236895/step/1',
                'https://stepik.org/lesson/236896/step/1',
                'https://stepik.org/lesson/236897/step/1',
                'https://stepik.org/lesson/236898/step/1',
                'https://stepik.org/lesson/236899/step/1',
                "https://stepik.org/lesson/236903/step/1",
                "https://stepik.org/lesson/236904/step/1",
                "https://stepik.org/lesson/236905/step/1"]



@pytest.mark.parametrize('links', parameters)
def test_questions(links, browser):
    browser.get(links)

    input = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'textarea[placeholder="Напишите ваш ответ здесь..."]')))
    answer = math.log(int(time.time()))
    input.send_keys(answer)

    button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
    button.click()

    #time.sleep(2000)

    output = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'p.smart-hints__hint')))
    message = output.text
    print(message)
    

    assert message == "Correct!", f'Error: expect message "Correct" get "{message}"!' 



