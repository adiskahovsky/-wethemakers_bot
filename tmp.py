import pymysql

conn = pymysql.connect(
            host='ftp70.hostland.ru',
            user='host1678429',
            password='494558ca',
            db='host1678429_mytestbd',
            charset='utf8mb4')


cursor = conn.cursor()
#cursor.execute("CREATE TABLE tasks (id INTEGER PRIMARY KEY AUTO_INCREMENT,last_name TEXT,name TEXT,telegram_id TEXT, task TEXT,data INTEGER,done TEXT)")
#cursor.execute("SELECT * FROM tasks WHERE done LIKE '0'")
#cursor.execute("SELECT last_name, name FROM tasks WHERE id LIKE {}".format(21))
#cursor.execute("SELECT last_name, name, task FROM tasks WHERE done LIKE '{}'".format('0'))

cursor.execute("UPDATE tasks SET done='{}' WHERE id={} ".format(str(1),str(10)))


#print(last_name)
conn.commit()
conn.close()


"""

import telebot
API_TOKEN = '600546248:AAEhltRhA6yqmnJbsxoBIwxS17NcQB4tGAI'
bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ =='__main__':
    bot.polling(none_stop=True,interval=0)


def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist




print(unique_list(['adis','adis','Kahovsky','Kahovsky']))"""