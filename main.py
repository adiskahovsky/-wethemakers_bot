
import config
import telebot
import SQL
import task
bot = telebot.TeleBot(config.API_TOKEN)
obj = SQL.SQL()


@bot.message_handler(commands=['task'])
def task(message):
    text = message.text
    id = str(message.chat.id)
    text = text.split()
    text.pop(0)
    for i in text:
        text= ' '
        text += str(i)

    print(text)
    obj.SQL_all(tel_id=id,task=str(text),data=3)

    print(id)
   
@bot.message_handler(commands=['all'])
def send_all(message):
    tel_id = str(message.chat.id)
    task_all = sql.SQL_all(tel_id,'0')
    bot.send_message(tel_id, task_all)

@bot.message_handler(commands=['stats'])
def send_stats(message):
    now = datetime.datetime.now()
	now_day = int(now.strftime("%j"))
	if(now_day > 7):
		late_date = now_day - 7
	else:
		#late = 1
		late_year = now.year - 1
		late_date = later_year.strftime("%j")
		late_year = datetime.datetime(now.year - 1, 12, 31, now.hour, now.minute, now.second)
		late_date = int(later_year.strftime("%j")) + now_day - 7

    tel_id = str(message.chat.id)
    task_stats = sql.SQL_stats(tel_id,'0',now_day,late_date)
    bot.send_message(tel_id, task_stats)

@bot.message_handler(commands=['done'])
def send_done(message):
    message = message.text
    task = message.split('/done')[1]
    tel_id = str(message.chat.id)
    sql.SQL_task(tel_id,task,done=1)






if __name__ =='__main__':
    bot.polling(none_stop=True,interval=0)


