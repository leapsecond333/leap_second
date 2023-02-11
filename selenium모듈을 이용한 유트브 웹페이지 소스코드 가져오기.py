from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions() # 자동으로 다운받은후 실행
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()),
    options=chrome_options)



url = 'https://namu.wiki/w/Pixelmon'
driver.get(url)             # 해당 url로 접속
driver.implicitly_wait(3)   # 인터넷정보 다 다운받을때까지 대기(초)


source_data = driver.page_source
for i in range(3):
    



























































