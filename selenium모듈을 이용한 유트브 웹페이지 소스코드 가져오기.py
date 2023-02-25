from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions() # 자동으로 다운받은후 실행
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()),
    options=chrome_options)



url = 'https://www.naver.com/'
driver.get(url)             # 해당 url로 접속
driver.implicitly_wait(3)   # 대기(초)

ID = 'leap_second@naver.com'
PW = 'leap_second333!'

login_button = driver.find_element(By.CLASS_NAME, 'link_login')
login_button.click()

driver.implicitly_wait(3)

login = driver.find_element(By.ID, 'id')
login.clear()
login.send_keys(ID)
login = driver.find_element(By.ID, 'pw')
login.clear()
login.send_keys(PW)
login.send_keys(Keys.ENTER)
driver.implicitly_wait(3)   # 대기(초)
