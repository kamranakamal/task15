from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# you need to download chromedriver and provide the path here


driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
time.sleep(5)

#selenium team deperecated find_element_by_xpath, use find_element(By.XPATH, value) instead
select_element = driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']")
select_element.send_keys("laptop")
select1 = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
list = driver.find_elements(By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")

print(f'Total items: {len(list)}')
for i in list:
    print(f'item: {i.text}')
driver.quit() 
