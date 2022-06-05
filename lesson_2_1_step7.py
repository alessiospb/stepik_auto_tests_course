import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(str(y))
    
    chckbx = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    chckbx.click()
	
    rb = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    rb.click()
	
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла