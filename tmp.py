import pymysql

conn = pymysql.connect(
            host='ftp70.hostland.ru',
            user='host1678429',
            password='494558ca',
            db='host1678429_mytestbd',
            charset='utf8mb4')


cursor = conn.cursor()
cursor.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY,telegram_id TEXT, task TEXT,done int)")



conn.commit()
conn.close()