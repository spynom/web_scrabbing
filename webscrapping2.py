from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.ajio.com/s/gold-and-silver-coins-4490-64441')
old_height=driver.execute_script('return document.body.scrollHeight')
while True:
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    new_hight=driver.execute_script('return document.body.scrollHeight')
    
    print(old_height,new_hight)
    if new_hight==old_height:
        break
    else:
        old_height=new_hight
html= driver.page_source

with open('ajio.html','w',encoding='utf-8') as f:
    f.write(html)

    