from selenuim import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(sevice=Service(
    ChromeDriverManager().install()),
    options=chrome_options)



url = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest'
driver.get(url)                 # 해당 url로 접속
time.sleep(3)                   # 대기(초)

click_url = driver.find_element(By.Class, '
