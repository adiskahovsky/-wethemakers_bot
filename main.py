
import config
import telebot

bot = telebot.TeleBot(config.API_TOKEN)



@bot.message_handler(content_types=['text'])
def echo_msg(message):
    bot.send_message(message.chat.id, message.text)

if __name__ =='__main__':
    bot.polling(none_stop=True,interval=0)


