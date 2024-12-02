from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# 사용자 계정 정보 입력
USER_ID = "your_username"  # 본인의 ID 입력
PASSWORD = "your_password"  # 본인의 비밀번호 입력

driver = webdriver.Chrome()
driver.get("https://www.bigkinds.or.kr/v2/news/index.do")




