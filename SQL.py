import pymysql

class SQL:
    def __init__(self):
        self.conn = pymysql.connect(
            host='ftp70.hostland.ru',
            user='host1678429',
            password='494558ca',
            db='host1678429_mytestbd',
            charset='utf8mb4'
        )

        self.cursor = self.conn.cursor()

    #cursor.execute("CREATE TABLE tasks(telegram_id varchar,task varchar,done int)")
    #cursor.execute("CREATE TABLE tasks (telegram_id TEXT, task TEXT,done int)")
    def SQL_all(self,tel_id,task,done=0):
        self.cursor.execte("insert into tasks(`{}`,`{}`,done)".format(tel_id,task,done))

    def SQL_done(self,id,done):
        self.cursor.execte("UPDATE tasks SET done = {} WHERE id ={}".format(done,id))

    def __del__(self):
        
        self.conn.commit()
        self.conn.close()