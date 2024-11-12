import requests

CLIENT_ID = "39Dyd_j190FDNYPtp1bx"
CLIENT_SECRET = "GvL1_naKcD"

encText = '''정보사 소속 요원, 중국 정보요원 추정 인물에 포섭돼 기밀 유출'''
url = f"https://openapi.naver.com/v1/search/news.json?query={encText}&sort=sim"

headers = {
    "X-Naver-Client-Id": CLIENT_ID,
    "X-Naver-Client-Secret": CLIENT_SECRET
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    response_body = response.text
    print(response_body)
else:
    print("Error Code:", response.status_code)