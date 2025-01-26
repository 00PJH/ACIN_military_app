import time
import os
from save_data_db import add_data
from bk_excel_crw import crw_news_excel
from bigkinds_row_modify import create_bk_news_data_name


def delete_file(file_path):
    """
    지정된 파일을 삭제하는 함수.
    파일이 존재하지 않을 경우 오류를 무시함.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"파일 삭제 완료: {file_path}")
        else:
            print(f"파일이 존재하지 않음: {file_path}")
    except Exception as e:
        print(f"파일 삭제 중 오류 발생: {e}")

def execute_periodically():
    """
    crw_news_excel 실행 -> 파일 삭제 -> add_data 실행을 1분 간격으로 반복.
    처음 루프에서는 파일 삭제를 생략.
    """
    

    while True:
        try:
            # 파일 경로 생성
            file_path = create_bk_news_data_name()
            print(f"확인 대상 파일 경로: {file_path}")

            # 파일이 존재하면 삭제
            if os.path.exists(file_path):
                print(f"파일이 존재합니다. 삭제를 진행합니다: {file_path}")
                delete_file(file_path)

            # 1. crw_news_excel 실행
            print("뉴스 Excel 크롤링 시작...")
            crw_news_excel()
            print("뉴스 Excel 크롤링 완료")

            # 2. add_data 실행
            print("데이터베이스에 데이터 추가 시작...")
            add_data()
            print("데이터베이스에 데이터 추가 완료")

            # 첫 번째 실행 완료 표시
            first_execution = False

        except Exception as e:
            print(f"작업 중 오류 발생: {e}")

        # # 1분 대기
        # print(" 1분 대기 시작...")
        # time.sleep(60)  # 6시간 = 21600초

       # 6시간 대기
        print("6시간 대기 시작...")
        time.sleep(6 * 60 * 60)  # 6시간 = 21600초

# 실행
if __name__ == "__main__":
    execute_periodically()