from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, date
import os
import time

# Selenium WebDriver 설정 (ChromeDriver 경로를 생략)
driver = webdriver.Chrome()
driver.maximize_window()

# URL 열기
url = "https://www.bigkinds.or.kr/v2/news/index.do"
open_url = driver.get(url)

# 페이지 로드 대기
time.sleep(2)  # 페이지가 로드될 시간을 충분히 대기 (필요 시 조정)

try:
    # 사이트 접속
    open_url

    # 로그인 영역에서 로그인 버튼 클릭
    login_area = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "login-area"))
    )
    login_button = login_area.find_element(By.CLASS_NAME, "btn-login")
    login_button.click()

    # ID 입력
    user_id_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-user-id"))
    )
    user_id_input.send_keys("wnsgud3738@naver.com")

    # 비밀번호 입력
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-user-password"))
    )
    password_input.send_keys("@pjh1514")

    # 로그인 버튼 클릭
    login_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-btn"))
    )
    login_submit_button.click()

    # 로그인 후 메인 페이지로 이동
    time.sleep(3)  # 로그인 처리가 완료될 때까지 잠시 대기
    driver.get("https://www.bigkinds.or.kr/v2/news/index.do")

    print("로그인 및 복귀 완료")

except Exception as e:
    print(f"오류 발생: {e}")


# "기간" 버튼 클릭
try:
    # "기간" 버튼을 기다렸다가 클릭
    period_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.tab-btn.search-tab_group[title='Open']"))
    )
    period_button.click()
    print("기간 버튼을 클릭했습니다.")
except Exception as e:
    print("버튼 클릭 실패:", e)

try:
    # label 태그와 연결된 input 요소를 클릭
    one_day_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='date1-7']"))
    )
    one_day_button.click()
    print("1일 버튼을 클릭했습니다.")
except Exception as e:
    print("1일 버튼 클릭 실패:", e)

try:
    calendar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img.ui-datepicker-trigger"))
    )
    calendar_button.click()
    print("달력 버튼을 클릭했습니다.")

    # 현재 날짜 클릭
    today_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "td.ui-datepicker-today a.ui-state-default"))
    )
    today_date.click()
    print("현재 날짜를 클릭했습니다.")
except Exception as e:
    print("실패:", e)

try:
    calendar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "img.ui-datepicker-trigger"))
    )
    calendar_button.click()
    print("달력 버튼을 클릭했습니다.")

    # 현재 날짜 클릭
    today_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "td.ui-datepicker-today a.ui-state-default"))
    )
    today_date.click()
    print("현재 날짜를 클릭했습니다.")
except Exception as e:
    print("실패:", e)

try:
    # "적용하기" 버튼 클릭
    apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-search.news-search-btn.news-report-search-btn"))
    )
    apply_button.click()
    print("적용하기 버튼을 클릭했습니다.")

except Exception as e:
    print("오류 발생:", e)    

try:
    button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-sm.btn-navy.step-3-click")
    driver.execute_script("arguments[0].click();", button)
    print("뉴스분석 버튼을 클릭했습니다.")
except Exception as e:
    print(f"버튼 클릭 오류: {e}")
    
try:
       # 엑셀 다운로드 버튼 로드 대기
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-wh.ml-auto.news-download-btn.mobile-excel-download"))
    )

    # move_to_element()로 버튼 위치로 이동
    actions = ActionChains(driver)
    actions.move_to_element(button).perform()

    # 버튼 로드 대기
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-wh.ml-auto.news-download-btn.mobile-excel-download"))
    )
    

    # JavaScript로 클릭
    driver.execute_script("arguments[0].click();", button)
    
    print("엑셀 다운로드 버튼 클릭 성공")
    time.sleep(20)
except Exception as e:
    print(f"엑셀 다운로드 버튼 클릭 오류: {e}")

finally:
    # 브라우저 닫기

    today = date.today()
    today_date = datetime.now().strftime("%Y%m%d") 
    file_name = ("NewsResult" + "_" + today_date + "-" + today_date  + ".xlsx")

    file_path = '/home/pjh/Downloads/' + file_name
    start_time = time.time()
    
    while time.time() - start_time < 5:
        if os.path.exists(file_path):
            print(f"파일이 존재합니다: {file_path}")
            driver.quit()
            time.sleep(1)  # 1초 대기 후 재확인
           
        else :
            print(f"파일이 존재하지 않습니다: {file_path}")
            
    