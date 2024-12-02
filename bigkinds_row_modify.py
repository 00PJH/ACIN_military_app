import pandas as pd
from datetime import date
from classification_title import load_csv_tokenizer, tokenize_encode, perform_inference, run
from summary_text import newSum

# 0. create file name
def create_bk_news_data_name():
    # 파일 이름 지정
    today = date.today()
    str_today = str(today.year) + str(today.month)  + str(today.day)
    input_file_path = ("NewsResult" + "_" + str_today + "-" + str_today  + ".xlsx")

    return input_file_path

# 1. extract only title
def extract_title_text_url(file_path):
    # excel 파일 읽기
    df = pd.read_excel(file_path)
    # 제목 열만 추출
    # df_titles_only = df[['제목']]
    # df_titles_only = df_titles_only.rename(columns={'제목':'title'})
    df_titles_URL = df[['제목','본문','URL']]
    df_titles_URL = df_titles_URL.rename(columns={'제목':'title'})
    df_test = df_titles_URL.head(500)
    # return df_titles_URL
    return df_test

# 2. classification titles
def classificatin_titles(input_df):
    prediction_titles = run(input_df)

    return prediction_titles

# 3. summary text
def sumText(text):
    sum_text = newSum(text)
    return sum_text

# 4. run module
def result_data(input_data_path):
    result_title = classificatin_titles(extract_title_text_url(input_data_path))
    reult_text = sumText

    
    # 1부터 시작하여 총 개수까지 index 재배열
    result.index = range(1, len(result) + 1)

    # return dataFrame object -> title, prediction
    return result
