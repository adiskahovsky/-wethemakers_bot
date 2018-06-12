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


    def SQL_all(self,tel_id,task,data,done='0'):

        self.cursor.execute("INSERT INTO tasks (telegram_id, task, data,done) VALUES ('{}','{}','{}','{}')".format(tel_id,task,data,done))
        self.conn.commit()

    def SQL_done(self,id,done):
        self.cursor.execte("UPDATE tasks SET done = {} WHERE id ={}".format(done,id))



    def __del__(self):

        self.conn.commit()
        self.conn.close()