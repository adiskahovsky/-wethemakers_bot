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

            self.cursor.execute("INSERT INTO tasks (last_name,name,telegram_id, task, data,done) VALUES ('{}','{}','{}','{}',{},{})".format(last_name,name,tel_id,task,data,done))
            self.conn.commit()

    def SQL_all(self,done):
        self.cursor.execute("SELECT last_name, name, task FROM tasks WHERE done LIKE '{}'".format(done))
        self.result = self.cursor.fetchall()
        return self.result

    def SQL_id(self,done):
        self.cursor.execute("SELECT id FROM tasks WHERE done LIKE '{}'".format(done))
        self.result = self.cursor.fetchall()
        return self.result

    def SQL_names(self,id):
        self.cursor.execute("SELECT last_name, name FROM tasks WHERE id LIKE {}".format(id))
        self.result = self.cursor.fetchall()
        return self.result

    def SQL_name_task(self,task):
        self.cursor.execute("SELECT name FROM tasks WHERE task LIKE '{}'".format(task))
        self.last_name = self.cursor.fetchall()
        return self.last_name

    def SQL_name_done(self,name):
        self.cursor.execute("SELECT done WHERE name LIKE '{}'".format(name))

        self.name = self.cursor.fetchall()
        return self.name





    def SQL_task_ln(self,last_name):
        self.cursor.execute("SELECT task FROM tasks WHERE last_name LIKE '{}' and done LIKE '0'".format(last_name))
        self.task = self.cursor.fetchall()
        return self.task

    def SQL_task_n(self,name):
        self.cursor.execute("SELECT task FROM tasks WHERE name LIKE '{}' and done LIKE '0'".format(name))
        self.task = self.cursor.fetchall()
        return self.task

    def SQL_done(self,tel_id,task,done,data,name,last_name):
        self.cursor.execute("INSERT INTO tasks (telegram_id, task, data, done, name, last_name) VALUES ('{}','{}','{}','{}','{}','{}')".format(tel_id,task,data,done,name,last_name))
        self.conn.commit()

    def SQL_statsall0(self,tel_id,now_day,late_date):
        done = str(0)
        self.cursor.execute("SELECT count(*) FROM tasks WHERE (`telegram_id` = {} and `done` = {}) and (data BETWEEN {} AND {})".format(tel_id,done,late_date,now_day))
        self.otvet = self.cursor.fetchone()
        return self.otvet

    def SQL_statsall1(self,tel_id,now_day,late_date):
        done = str(1)
        self.cursor.execute("SELECT count(*) FROM tasks WHERE (`telegram_id` = {} and `done` = {}) and (data BETWEEN {} AND {})".format(tel_id,done,late_date,now_day))
        self.otvet = self.cursor.fetchone()
        return self.otvet

    def SQL_stats0(self,tel_id,now_day,late_date,name,last_name):
        done = str(0)
        self.cursor.execute("SELECT count(*) FROM tasks WHERE (`telegram_id` = {} and `done` = {} and `name` = '{}' and `last_name` = '{}') and (data BETWEEN {} AND {})".format(tel_id,done,name,last_name,late_date,now_day))
        self.otvet = self.cursor.fetchone()
        return self.otvet

    def SQL_stats1(self,tel_id,now_day,late_date,name,last_name):
        done = str(1)
        self.cursor.execute("SELECT count(*) FROM tasks WHERE (`telegram_id` = {} and `done` = {} and `name` = '{}' and `last_name` = '{}') and (data BETWEEN {} AND {})".format(tel_id,done,name,last_name,late_date,now_day))
        self.otvet = self.cursor.fetchone()
        return self.otvet

    def SQL_task_done(self, last_name,name):
        self.cursor.execute("SELECT task FROM tasks WHERE name LIKE '{}' and last_name LIKE '{}' and done LIKE '0'".format(name,last_name))
        self.last_name = self.cursor.fetchall()
        return self.last_name

    def SQL_done_id(self,last_name,name):
        self.cursor.execute("SELECT id FROM tasks WHERE name LIKE '{}' and last_name LIKE '{}' and done LIKE '0'".format(name,last_name))
        self.last_name = self.cursor.fetchall()
        return self.last_name


    def SQL_done_id_1(self,id):
        self.cursor.execute("UPDATE tasks SET done='{}' WHERE id={} ".format(str(1),id))
        self.conn.commit()

    def __del__(self):

        self.conn.commit()
        self.conn.close()
