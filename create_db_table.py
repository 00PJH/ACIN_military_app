import pymysql

db = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '1514',
        port = 3306,
        db = 'acin',
        charset = 'utf8'
    )

cursor = db.cursor()

sql = '''
    CREATE TABLE news(
        title varchar(100) ,
        text VARCHAR(300),
        URL VARCHAR(200),
        PRIMARY KEY(title)
    )
'''

cursor.execute(sql)
db.commit()
db.close()