
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






if __name__ =='__main__':
    bot.polling(none_stop=True,interval=0)


