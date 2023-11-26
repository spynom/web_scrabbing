from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.smartprix.com/mobiles')
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/span').click()
driver.find_element(by=By.XPATH,value='//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/span').click()

old_height= driver.execute_script('return document.body.scrollHeight')
while True:
    
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(5)
    new_height= driver.execute_script('return document.body.scrollHeight')
    print(old_height,new_height)
    if new_height==old_height:
        break
    else: old_height=new_height
html =driver.page_source

with open('mobile.html','w',encoding='utf-8') as f:
    f.write(html)

