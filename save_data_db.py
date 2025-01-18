import pymysql
import pandas as pd
from bigkinds_row_modify import create_bk_news_data_name,extract_title_text_url, classificatin_titles,result_data


def add_data():
    db = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '1514',
        port = 3306,
        db = 'acin',
        charset = 'utf8'
    )

    df = result_data(create_bk_news_data_name())
    

    try:
        with db.cursor() as cursor:
            for _, row in df.iterrows():

                title = row['title'] if pd.notna(row['title']) else None
                text = row['본문'] if pd.notna(row['본문']) else None
                url = row['URL'] if pd.notna(row['URL']) else None
                

                sql = """
                    INSERT INTO news (title, text, URL)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        text = VALUES(text),
                        URL = VALUES(URL)
                """
                cursor.execute(sql, (title, text, url))
            db.commit()

            print("Data inserted successfully!")
    finally:
        db.close()


# bk_news excel file -> title, predictions, url-> classification -> add data & commit db

