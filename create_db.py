import pymysql

db = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '1514',
        port = 3306,
        db = 'acin_news_app',
        charset = 'utf8'
    )

cursor = db.cursor()

sql = '''
    CREATE TABLE classification(
        title varchar(100) ,
        URL TEXT,
        predictions tinyint,
        PRIMARY KEY(title)
    )
'''

cursor.execute(sql)
db.commit()
db.close()