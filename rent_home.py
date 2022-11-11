import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

#Решение задачи с домом по 100$


def calc(x):
    # Посчитать математическую функцию от x.
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID,value='input_value')
    x = x_element.text
    y = calc(x)
    print(x)
    print(y)
    input1 = browser.find_element(By.ID,value='answer')
    input1.send_keys(y)

    button = browser.find_element(By.ID, 'solve')
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()