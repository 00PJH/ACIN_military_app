import pandas as pd
from datetime import date
from classification_title import load_csv_tokenizer, tokenize_encode, perform_inference, run

# 파일 이름 지정
today = date.today()
str_today = str(today.year) + str(today.month)  + str(today.day)
input_file_path = ("NewsResult" + "_" + str_today + "-" + str_today  + ".xlsx")

# 1. extract only title
def extract_title(file_path):
    # excel 파일 읽기
    df = pd.read_excel(file_path)
    # 제목 열만 추출
    df_titles_only = df[['제목']]
    df_titles_only = df_titles_only.rename(columns={'제목':'title'})

    df_test = df_titles_only.head(30)

    return df_test

# 2. classification titles
def classificatin_titles(input_df):
    prediction_titles = run(input_df)

    return prediction_titles

# 3. run module
def main(input_data_path):
    result = classificatin_titles(extract_title(input_data_path))

    return result

print(main(input_file_path))