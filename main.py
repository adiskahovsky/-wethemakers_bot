import time
import datetime
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
    name = message.from_user.first_name
    last_name = message.from_user.last_name


    print(name)

    text = text.split()
    text.pop(0)
    result =''
    for i in text:

        result += str(i) + ' '

    now = datetime.datetime.now()
    now_day = int(now.strftime("%j"))
    data = now_day
    print(result)
    obj.SQL_add_task(tel_id=id,task=str(result),data=data,name=name,last_name=last_name)

    print(id)

@bot.message_handler(commands=['all'])
def task(message):

    result = obj.SQL_id(0)
    print(result)
    names=[]
    for i in result:
        for j in i:
            names.append(obj.SQL_names(j))

    print(names)
    names = unique_list(names)
    print(names)
    strr=''
    print('46')
    for i in names:
        for j in i:
            print('49')
            if(str_list(obj.SQL_task_ln(j[0]))==str_list(obj.SQL_task_n(j[1]))):
                print('51')
                strr+='\n'+'📋'+j[0]
                strr+=j[1]+' '
                strr+=" opens's tasks: "+'\n'
                result = obj.SQL_task_ln(j[0])
                for k in result:
                    for n in k:
                        strr +='⭕'+n+'\n'
    bot.send_message(message.chat.id,strr)
    print(strr)
"""
@bot.message_handler(commands=['stats'])
def send_stats(message):
    now = datetime.datetime.now()
    now_day = int(now.strftime("%j"))
    tel_id = str(message.chat.id)
    bot.send_message(tel_id, now_day)
    if(now_day > 7):
        late_date = now_day - 7
    else:
		#late = 1
        late_year = now.year - 1
        late_date = later_year.strftime("%j")
        late_year = datetime.datetime(now.year - 1, 12, 31, now.hour, now.minute, now.second)
        late_date = int(later_year.strftime("%j")) + now_day - 7

    task_stats = sql.SQL_stats(tel_id,'0',now_day,late_date)
    if(task_stats):
        messageanswer = ''
        rang = 0
        ResultList = task_stats
        for value in ResultList:
            if(rang == 0):
                smile = "📋"
            else:
                smile = "⭕️"
            messageanswer = messageanswer + smile + value + '\n'
            rang = rang + 1
            bot.send_message(tel_id, messageanswer)
    else:
        bot.send_message(tel_id, 'Записей не найдено')
		
		
@bot.message_handler(commands=['done'])
def send_done(message):
	task = message.text.split('/done')[1]
	now = datetime.datetime.now()
	now_day = int(now.strftime("%j"))
	done = "1"
	data = now_day
	tel_id = str(message.chat.id)
	sql.SQL_done(tel_id,task,done,data)
"""
"""
    result=obj.SQL_all(0)

   result_str=[]
   tasks= []
   names = []
   for i in list(result):
      # i=list(i)
      # i.pop()
       tasks.append(i[2].split())
       names.append([i[0],i[1]])
       for j in i:
           result_str.append(j)

   strr=''
   for i in names:
       for j in tasks:
           strr+=i[0]+' '
           strr+=i[1]+' '
           if ((str(i[0])[0] + str(i[1])[0]) *2) == j[0]:
               strr+=j[1]+' '


   strr = strr.split()
   print(strr)
   strr = unique_list(strr)
   result =''
   for i in strr:

       result+=i+' '

   print(result)
   #print(result)

   bot.send_message(message.chat.id,result)
"""






def str_list(l):
    result=[]
    for i in l:
        for j in i:
            result.append(j)

    return result

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist


"""
@bot.message_handler(commands=['all'])
def send_all(message):
   tel_id = str(message.chat.id)
   task_all = SQL.SQL_all(tel_id,'0')
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


"""



if __name__ =='__main__':
    bot.polling(none_stop=True,interval=0)


