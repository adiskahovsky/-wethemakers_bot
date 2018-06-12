"""import pymysql

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
"""



import telebot
API_TOKEN = '600546248:AAEhltRhA6yqmnJbsxoBIwxS17NcQB4tGAI'
bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ =='__main__':
    bot.polling(none_stop=True,interval=0)