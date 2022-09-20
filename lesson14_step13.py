from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestWeb(unittest.TestCase):
    def test_web1(self):
        self.assertEqual(selenium_script('http://suninjuly.github.io/registration1.html'),
        "Congratulations! You have successfully registered!", "Test1 Web1 ERROR")

    def test_web2(self):
        self.assertEqual(selenium_script('http://suninjuly.github.io/registration2.html'),
        "Congratulations! You have successfully registered!", "Test2 Web2 ERROR")

def selenium_script(link):
    browser = webdriver.Chrome()
    browser.get(link)

        # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first.form-control')
    input1.send_keys("lol)")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second.form-control')
    input2.send_keys("lol)")
    input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third.form-control')
    input3.send_keys("lol)")

        # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
    time.sleep(1)

        # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

        # закрываем браузер после всех манипуляций
    browser.quit()    

if __name__ == "__main__":

   unittest.main()