from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(ChromeDriverManager().install())



driver.get('https://www.google.com')
time.sleep(2)
google_search=driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
google_search.send_keys('campusx')
time.sleep(3)
google_search.send_keys(Keys.ENTER)

time.sleep(2)
link=driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[2]/div/div/div[1]/div/div/span/a/h3')
link.click()


time.sleep(2)
link=driver.find_element(by=By.XPATH,value='//*[@id="1668425005116"]/h1[2]')
link.click()