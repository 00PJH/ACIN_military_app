from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pymysql

def crw_bk_title_text_url(input_url):
    # Selenium WebDriver 설정 (ChromeDriver 경로를 생략)
    driver = webdriver.Chrome()

    # URL 열기
    
    driver.get(input_url)

    # 페이지 로드 대기
    time.sleep(5)  # 페이지가 로드될 시간을 충분히 대기 (필요 시 조정)

    # 스크롤 다운으로 동적 콘텐츠 로드
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # 추가 대기

    texts = []
    # 데이터 크롤링
    articles = driver.find_elements(By.CSS_SELECTOR, "div.cont.news-detail")
    for article in articles:
        try:
            title = article.find_element(By.CSS_SELECTOR, "strong.title").text
            summary = article.find_element(By.CSS_SELECTOR, "p.text").text
            link = article.find_element(By.CSS_SELECTOR, "div.info").find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        except Exception as e:
            title, summary, link = "N/A", "N/A", "N/A"

        texts.append(summary)
        print(f"제목: {title}")
        print(f"본문: {summary}")
        print(f"원문 링크: {link}")
        print("-" * 50)

    # 드라이버 종료
    driver.quit()

# def add_data():
#     db = pymysql.connect(
#         host = 'localhost',
#         user = 'root',
#         password = '1514',
#         port = 3306,
#         db = 'acin_news_app',
#         charset = 'utf8'
#     )

#     df = result_data(create_bk_news_data_name())

#     try:
#         with db.cursor() as cursor:
#             for _, row in df.iterrows():

#                 title = row['title'] if pd.notna(row['title']) else None
#                 url = row['URL'] if pd.notna(row['URL']) else None
#                 predictions = row['predictions']

#                 sql = """
#                     INSERT INTO classification (title, URL, predictions)
#                     VALUES (%s, %s, %s)
#                 """
#                 cursor.execute(sql, (title, url, predictions))
#             db.commit()

#             print("Data inserted successfully!")
#     finally:
#         db.close()

url = "https://www.bigkinds.or.kr/v2/news/recentNews.do"
crw_bk_title_text_url(url)