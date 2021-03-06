import time
import datetime
import config
import telebot
import SQL
import task
from telebot import  types
from telebot.types import Update

import re
bot = telebot.TeleBot(config.API_TOKEN)
obj = SQL.SQL()


@bot.message_handler(commands=['all'])
def task(message):

    if(len(obj.SQL_task_ln(message.from_user.last_name)))==len((obj.SQL_task_n(message.from_user.first_name))):
        name = message.from_user.last_name + ' ' + message.from_user.first_name
        result = obj.SQL_task_ln(message.from_user.last_name)
        strr=''
        print('51')
        strr+='\n'+'📋 '+name + ' '

        strr+=" open tasks: "+'\n'
        for k in result:
            for n in k:
                strr +='⭕ '+n+'\n'
        bot.send_message(message.chat.id,strr)

@bot.message_handler(commands=['task'])
def task(message):
	text = message.text
	id = str(message.chat.id)
	name = message.from_user.first_name
	last_name = message.from_user.last_name
	# if(name):
	# 	pass
	# else:
	# 	name = ''

	# if(last_name):
	# 	pass
	# else:
	# 	last_name = ''

	print(name)

	text = text.split()
	text.pop(0)
	if(text):
		result =''
		for i in text:

		    result += str(i) + ' '

		now = datetime.datetime.now()
		now_day = int(now.strftime("%j"))
		data = now_day
		print(result)

		obj.SQL_add_task(tel_id=id,task=str(result),data=data,name=name,last_name=last_name)

		text2=''
		for i in text:
		    text2+=i+' '
		bot.send_message(message.chat.id,'⭕ {} added task: {}'.format(message.from_user.last_name+' '+
		                                                              message.from_user.first_name,text2))
		print(id)
	else:
		bot.send_message(message.chat.id, 'You did not enter a task name')

@bot.message_handler(commands=['all'])
def task(message):

    if(len(obj.SQL_task_ln(message.from_user.last_name)))==len((obj.SQL_task_n(message.from_user.first_name))):
        name = message.from_user.last_name + ' ' + message.from_user.first_name
        result = obj.SQL_task_ln(message.from_user.last_name)
        strr=''
        print('51')
        strr+='\n'+'📋 '+name + ' '

        strr+=" open tasks: "+'\n'
        for k in result:
            for n in k:
                strr +='⭕ '+n+'\n'
        bot.send_message(message.chat.id,strr)




    """
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
                strr+='\n'+'📋'+j[0] + ' '
                strr+=j[1]+' '
                strr+=" opens's tasks: "+'\n'
                result = obj.SQL_task_ln(j[0])
                for k in result:
                    for n in k:
                        strr +='⭕'+n+'\n'
    bot.send_message(message.chat.id,strr)
    print(strr)
    """

@bot.message_handler(commands=['statsall'])
def send_stats(message):
    now = datetime.datetime.now()
    now_day = int(now.strftime("%j"))
    tel_id = str(message.chat.id)
    if(now_day > 7):
        late_date = now_day - 7
    else:
		#late = 1
        late_year = now.year - 1
        late_date = later_year.strftime("%j")
        late_year = datetime.datetime(now.year - 1, 12, 31, now.hour, now.minute, now.second)
        late_date = int(later_year.strftime("%j")) + now_day - 7

    task_stats0 = obj.SQL_statsall0(tel_id,now_day,late_date)
    task_stats1 = obj.SQL_statsall1(tel_id,now_day,late_date)
    if(task_stats0 or task_stats1):
        messageanswer0 = task_stats0[0]
        messageanswer1 = task_stats1[0]
        print(messageanswer0)
        print(messageanswer1)
        if(messageanswer0 < 2):
            text0 = ' task'
        else:
            text0 = ' tasks'

        if(messageanswer1 < 2):
            text1 = ' task'
        else:
            text1 = ' tasks'
        messageanswer = '📋  Week summary of all: \n✅ Completed: ' + str(messageanswer1) + text0 + '\n' + '⭕️ Open tasks: ' + str(messageanswer0) + text1
        bot.send_message(tel_id, messageanswer)
    else:
        bot.send_message(tel_id, 'No task found')

@bot.message_handler(commands=['stats'])
def send_stats(message):
    now = datetime.datetime.now()
    now_day = int(now.strftime("%j"))
    tel_id = str(message.chat.id)
    name = message.from_user.first_name
    last_name = message.from_user.last_name
    if(now_day > 7):
        late_date = now_day - 7
    else:
		#late = 1
        late_year = now.year - 1
        late_date = later_year.strftime("%j")
        late_year = datetime.datetime(now.year - 1, 12, 31, now.hour, now.minute, now.second)
        late_date = int(later_year.strftime("%j")) + now_day - 7

    task_stats0 = obj.SQL_stats0(tel_id,now_day,late_date,name,last_name)
    task_stats1 = obj.SQL_stats1(tel_id,now_day,late_date,name,last_name)
    if(task_stats0 or task_stats1):
        messageanswer0 = task_stats0[0]
        messageanswer1 = task_stats1[0]
        print(messageanswer0)
        print(messageanswer1)
        if(messageanswer0 < 2):
            text0 = ' task'
        else:
            text0 = ' tasks'

        if(messageanswer1 < 2):
            text1 = ' task'
        else:
            text1 = ' tasks'
        messageanswer = '📋' + name + ' ' + last_name + ' weekly\ntasks summary: \n✅ Completed: ' + str(messageanswer1) + text0 + '\n' + '⭕️ Open tasks: ' + str(messageanswer0) + text1
        bot.send_message(tel_id, messageanswer)
    else:
        bot.send_message(tel_id, 'No task found')


@bot.message_handler(commands=['done'])
def send_done(message):
	task = message.text.split('/done')[1]
	tel_id = str(message.chat.id)
	name = message.from_user.first_name
	last_name = message.from_user.last_name
	# if(name):
	# 	pass
	# else:
	# 	name = ''
		
	# if(last_name):
	# 	pass
	# else:
	# 	last_name = ''

	if(task):
		now = datetime.datetime.now()
		now_day = int(now.strftime("%j"))
		done = 1
		data = now_day
		obj.SQL_done(tel_id,task,done,data,name,last_name)
		bot.send_message(tel_id, '✅ ' + name + ' ' + last_name +  ' completed:\n' + task)
	else:
		bot.send_message(tel_id, 'You did not enter a task name')

@bot.inline_handler(func=lambda query: True)
def query_text(query):

	digits_pattern= re.compile(r'^[0-9]+ [0-9]+$', re.MULTILINE)
	digits_pattern = re.compile(r'^$', re.MULTILINE)
	print("Пашет")
	try:
		print(query.from_user.last_name)
		last_name = query.from_user.last_name
		first_name = query.from_user.first_name
		# if(first_name):
		# 	pass
		# else:
		# 	first_name = ''
			
		# if(last_name):
		# 	pass
		# else:
		# 	last_name = ''

		print('ok')
		matches = re.match(digits_pattern, query.query)
		num1  = matches.group().split()
		print('ok2')
		print(num1)
		result2=[]

		result = obj.SQL_task_done(last_name=last_name,name=first_name)
		for i in result:
		    for j in i:
		        result2.append(j)
		result_list = []
		print(result2)


		k=0
		ids = obj.SQL_done_id(last_name=last_name,name=first_name)


		ids_list=[]
		for i in ids:
		    for j in i:
		        ids_list.append(j)

		for i in result2:
		    result_list.append(
		        types.InlineQueryResultArticle(str(ids_list[k]), '{}'.format(i), types.InputTextMessageContent('Task completed {}'.format(str(ids_list[k]))), None,
		                                       '', True, ''.format(str(ids_list[k])),
		                                       '', 640, 640))
		    k+=1
		print('ok3')

		m_sub = num1
		print('ok4')

		print(query)
		bot.answer_inline_query(query.id,result_list,cache_time=1)
	except AttributeError as ex:
		print("FUCKKKK")
		return


@bot.message_handler(content_types=['text'])
def send_done(message):
    print(message.text)
    text = message.text
    text = text.split()
    if(text[0]=='Task' and text[1]=='completed'):

        bot.delete_message(message.chat.id,message.message_id)
        print('True')
        text.pop(0)
        text.pop(0)
        print(text)
        reseult_text =''
        for i in text:
            reseult_text+=i

        print(reseult_text)
        result = obj.SQL_last_data(reseult_text)
        print(result)
        obj.SQL_done_id_1(reseult_text)
        reseult_text=[]
        for i in result:
            for j in i:
                reseult_text.append(j)
        print(reseult_text)
        if(reseult_text[0] !='' and reseult_text[1] !='' and reseult_text[2] !=''):
        	bot.send_message(message.chat.id,'✅ {} {} completed: {}'.format(reseult_text[0] ,reseult_text[1],reseult_text[2]))
        elif(reseult_text[0] !='' and reseult_text[1] !=''):
        	bot.send_message(message.chat.id,'✅ {} {} completed: {}'.format(reseult_text[0] ,reseult_text[1]))
        elif(reseult_text[0] !=''):
        	bot.send_message(message.chat.id,'✅ {} {} completed: {}'.format(reseult_text[0]))
"""
@bot.inline_handler(func=lambda query: True)
def query_text(inline_query):
    print(inline_query)
    try:
        r_sub = types.InlineQueryResultArticle(
            id='id', title="Задача",
            description="(текст задачи)",
            input_message_content=types.InputTextMessageContent(
            message_text="Задача отмечена как выполненная")


            bot.answer_inline_query(inline_query.id, r_sub)
    except Exception as e:
        print(e)



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
