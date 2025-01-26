import pandas as pd
from datetime import datetime, date
from classification_title import load_csv_tokenizer, tokenize_encode, perform_inference, run
from summary_text import newSum
from sqlalchemy import create_engine

####### batch #########
def process_in_batches(df, num_batches, process_function):
    """
    DataFrame을 지정된 배치 수로 나누어 처리하는 함수.

    Args:
        df (pd.DataFrame): 입력 DataFrame
        num_batches (int): 나눌 배치의 개수
        process_function (function): 각 배치에 대해 수행할 함수

    Returns:
        pd.DataFrame: 처리된 결과를 병합한 DataFrame
    """
    batch_size = (len(df) + num_batches - 1) // num_batches  # 배치 크기 계산 (올림 처리)
    processed_batches = []  # 처리된 배치들을 저장할 리스트

    for i in range(0, len(df), batch_size):
        batch_end = min(i + batch_size, len(df))  # 현재 배치의 끝 인덱스 계산
        batch = df.iloc[i:batch_end]  # 배치 추출

        print(f"Processing batch {i // batch_size + 1}: rows {i} to {batch_end - 1}")

        # 배치에 대해 처리 함수 호출
        processed_batch = process_function(batch)
        processed_batches.append(processed_batch)  # 처리된 배치를 리스트에 추가

    # 처리된 배치들을 병합하여 반환
    return pd.concat(processed_batches, ignore_index=True)

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
    print("extract title, text, url start")
    df_titles_texts_URL = df[['제목','본문','URL']]
    df_titles_texts_URL = df_titles_texts_URL.rename(columns={'제목':'title'})

    # # ### 테스트용 50개 추출
    # df_test = df_titles_texts_URL.head(100)
    print("extract title, text, url end")
    # return df_test

    return df_titles_texts_URL

# 2. classification titles
def classificatin_titles(input_df):
    print("classification title start")
    prediction_titles = run(input_df)

    print("classification title end")
    return prediction_titles

# 3. summary text
def summarize_batch(batch):
    """
    배치 내 본문을 요약하는 예제 함수.

    Args:
        batch (pd.DataFrame): 입력 배치 DataFrame

    Returns:
        pd.DataFrame: 요약된 결과를 포함한 DataFrame
    """
    # 요약 작업 (여기서 newSum 함수는 BERT 요약 함수라고 가정)
    for idx in batch.index:
        batch.at[idx, '본문'] = newSum(batch.at[idx, '본문'])

    return batch

# 4. run module
def result_data(input_data_path):
    result_title = classificatin_titles(extract_title_text_url(input_data_path))

    print(f"DataFrame 전체 행 개수: {len(result_title)}")
    # 배치 처리 실행
    num_batches = 50  # 배치 수
    print("summary text start")
    processed_df = process_in_batches(result_title, num_batches, summarize_batch)
    
    print("summary text end")
    # return dataFrame object -> title, prediction
    return result_title
