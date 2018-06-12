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


    def SQL_add_task(self,last_name,name,tel_id,task,data,done='0'):

        if last_name is not None and name is not None:
            self.task = str(last_name[0]+name[0]+last_name[0]+name[0]+' '+task)

            self.cursor.execute("INSERT INTO tasks (last_name,name,telegram_id, task, data,done) VALUES ('{}','{}','{}','{}',{},{})".format(last_name,name,tel_id,self.task,data,done))
            self.conn.commit()

    def SQL_all(self,done):
        self.cursor.execute("SELECT last_name, name, task FROM tasks WHERE done LIKE '{}'".format(done))
        self.result = self.cursor.fetchall()
        return self.result


    def SQL_done(self,id,done):
        self.cursor.execte("UPDATE tasks SET done = {} WHERE id ={}".format(done,id))

    """

  def SQL_all(self,tel_id,done):
      self.cursor.execute("SELECT * FROM tasks WHERE telegram_id={} and done ={}".format(tel_id,done))
      otvet = cursor.fetchone()
      return otvet

  def SQL_stats(self,tel_id,done,now_day,late_date):
      self.cursor.execute("SELECT * FROM tasks WHERE telegram_id = {} and done = {} and `date` >= {} and `date` <= {}".format(tel_id,done,now_day,late_date))
      otvet = cursor.fetchone()
      return otvet
"""


    def __del__(self):

        self.conn.commit()
        self.conn.close()
