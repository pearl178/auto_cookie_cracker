import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/pearllll/Development/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('https://orteil.dashnet.org/cookieclicker/')
English = driver.find_element(By.ID, 'langSelect-EN')
English.click()

# Cookie Image
out_timeout = time.time() + 60*5
big_cookie = driver.find_element(By.CSS_SELECTOR, '#bigCookie')
while time.time() < out_timeout:
    in_timeout = time.time() + 5
    while time.time() < in_timeout:
        big_cookie.click()
    product_price_tags = driver.find_elements(By.CSS_SELECTOR, '.enabled')
    product_price_tags[-1].click()

# Cookie Number
cookie_numbers = driver.find_element(By.CSS_SELECTOR, '#cookies')
cookie_rate = cookie_numbers.text.split(':')[1]
print(f"cookies/second: {cookie_rate}")