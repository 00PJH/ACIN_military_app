import pandas as pd
from datetime import datetime, date
from classification_title import load_csv_tokenizer, tokenize_encode, perform_inference, run
from summary_text import newSum

# 0. create file name
def create_bk_news_data_name():
    # 파일 이름 지정
    today = date.today()
    today_date = datetime.now().strftime("%Y%m%d") 
    file_name = ("NewsResult" + "_" + today_date + "-" + today_date  + ".xlsx")

    input_file_path = '/home/pjh/Downloads/' + file_name

    return input_file_path

# 1. extract only title
def extract_title_text_url(file_path):
    # excel 파일 읽기
    df = pd.read_excel(file_path)
    # 제목 열만 추출
    # df_titles_only = df[['제목']]
    # df_titles_only = df_titles_only.rename(columns={'제목':'title'})
    df_titles_texts_URL = df[['제목','본문','URL']]
    df_titles_texts_URL = df_titles_texts_URL.rename(columns={'제목':'title'})

    # ### 테스트용 50개 추출
    # df_test = df_titles_texts_URL.head(100)
    print("extract title, text, url")
    # return df_test

    return df_titles_texts_URL

# 2. classification titles
def classificatin_titles(input_df):
    prediction_titles = run(input_df)

    print("classification title")
    return prediction_titles

# 3. run module
def result_data(input_data_path):
    result_title = classificatin_titles(extract_title_text_url(input_data_path))

    news_text_list = result_title['본문'].to_list()

     # 1부터 시작하여 총 개수까지 index 재배열
    result_title.index = range(len(result_title))

    for idx, e in enumerate(news_text_list):
        result_title.at[idx, '본문'] = newSum(e)
    
    print("summary text")
    # return dataFrame object -> title, prediction
    return result_title
