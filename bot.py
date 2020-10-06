import telebot
import config
import json
import random
import words

#Подключаю телеграм
from telebot import types
from datetime import datetime
from pathlib import Path

bot = telebot.TeleBot(config.TOKEN)

# Вывод информации о запуске
print('the bot was launched')
# Переменные
version = '0.1'
category = []
words_d = words.words_d
words_e = words.words_e
words_f = words.words_f
words_w = words.words_w
words_t = words.words_t
ids = []
answer = []
# Перевод в String
words_str = str(len(words_d)+len(words_e)+len(words_f)+len(words_w)+len(words_t))
# Клавиатура стандарт
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("📓 Урок")
item2 = types.KeyboardButton("📒 Игра")
item3 = types.KeyboardButton("👤 Профиль")
item4 = types.KeyboardButton("ℹ Информация")
#item5 = types.KeyboardButton("💳 Пожертвовать")
item10 = types.KeyboardButton("🎖 Награды")
markup.add(item1, item2, item3, item4, item10)
# Клавиатура Урока
lesson1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item6 = types.KeyboardButton("📓 Новые слова")
item7 = types.KeyboardButton("📗        Тесты")
item8 = types.KeyboardButton("📕 Повторение")
item9 = types.KeyboardButton("🔙 Назад")
lesson1.add(item6, item7, item8, item9)
#Клавиатура выбора урока
lesson = types.ReplyKeyboardMarkup(resize_keyboard=True)
li1 = types.KeyboardButton("🛁 Повседневные")
li2 = types.KeyboardButton("📕 Образование")
li3 = types.KeyboardButton("🍔 Еда")
li4 = types.KeyboardButton("👔 Одежда")
li5 = types.KeyboardButton("✈ Путешествия")
li6 = types.KeyboardButton("↩️ Назад")
lesson.add(li1, li2, li3, li4, li5, li6)
#Клавиатура выбора урока
nwords = types.ReplyKeyboardMarkup(resize_keyboard=True)
item11 = types.KeyboardButton("🚰 Повседневные")
item12 = types.KeyboardButton("📖 Образование")
item13 = types.KeyboardButton("🍜 Еда")
item14 = types.KeyboardButton("👕 Одежда")
item15 = types.KeyboardButton("🚢 Путешествия")
item16 = types.KeyboardButton("↩️ Назад")
nwords.add(item11, item12, item13, item14, item15, item16)
#Клавиатура выбора теств
test = types.ReplyKeyboardMarkup(resize_keyboard=True)
item17 = types.KeyboardButton("👋 Повседневные")
item18 = types.KeyboardButton("📚 Образование")
item19 = types.KeyboardButton("🍟 Еда")
item20 = types.KeyboardButton("👗 Одежда")
item21 = types.KeyboardButton("🌴 Путешествия")
item22 = types.KeyboardButton("↩️ Назад")
test.add(item17, item18, item19, item20, item21, item22)
#Игра
game = types.ReplyKeyboardMarkup(resize_keyboard=True)
item23 = types.KeyboardButton("🎮 Игра")
item24 = types.KeyboardButton("🏅 Рейтинг")
item25 = types.KeyboardButton("🔙 Назад")
game.add(item23, item24, item25)
#Приветствие после /start
@bot.message_handler(commands=['start']) 
def  welcome(message):
	uname = message.chat.username
	filename = Path("./users/" + uname+".txt")
	# myfile = open(filename, mode='r')
	# jdata = json.load(myfile)
	# reg = int(jdata['reg'])
	tst = filename.exists()
	if tst == 0:
		bot.send_message(message.chat.id, '• Здраствуйте! \n• Я бот-учитель английского языка \n• Для начала урока нажмите на кнопку 📓 Урок', reply_markup=markup)
		#Присвоение username -> uname
		uname = message.chat.username
		iduser = str(message.chat.id)
		now = datetime.now()
		#Сохранение профиля
		filename = "./users/" + uname+".txt"
		myfile = open(filename, mode='w')
		pro_file = {
		'username': uname,
		'ID': iduser,
		'data': datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S"),
		'lvl': 0,
		'xp': 0,
		'daily': 0,
		'education': 0,
		'food': 0,
		'wear': 0,
		'travel': 0,
		'reg':1,
		'admin': 0,
		'reward': 'no'
		}
		json.dump(pro_file, myfile)
		myfile.close ()
		#Сохранение статистики
		filename = "statistics.txt"
		myfile = open(filename, mode='r')
		jdata = json.load(myfile)
		regis = str(jdata['registered'])
		regisint = int(regis) + 1
		regisstr = str(regisint)
		myfile.close ()
		filename = "statistics.txt"
		myfile = open(filename, mode='w')
		quantity_regs = {
		'registered': regisstr,
		'test': 0
		}
		json.dump(quantity_regs, myfile)
		myfile.close ()
		#Вывод в консоль
		print('new user: '+ uname)
		print('ID: '+ iduser)
		print('registered: ' + regisstr)
	else:
		bot.send_message(message.chat.id, '👋 С возвращением!', reply_markup=markup)

#Логика бота
# def newdaily(message):
# 	uname = message.chat.username
# 	filename = "./users/" + uname+".txt"
# 	myfile = open(filename, mode='r')
# 	nwd_data = json.load(myfile)
# 	xp = str(nwd_data['xp'])
# 	lvl = str(nwd_data['lvl'])
# 	daily = str(nwd_data['daily'])
# 	education = str(nwd_data['education'])
# 	food = str(nwd_data['food'])
# 	wear = str(nwd_data['wear'])
# 	travel = str(nwd_data['travel'])
# 	reg = str(nwd_data['reg'])
# 	myfile.close ()

# 	global category
# 	for x in range(0, len(ids)):
# 		if ids[x] == message.chat.id:
# 			category[x] = 6
# 	global task
# 	task = int(daily) + 1
# 	for x in range(0, len(ids)):
# 		if ids[x] == message.chat.id:
# 			while words_d[task][0] == answer[x]:
# 				task = daily
# 	ru, eng = words_d[task]
# 	for x in range(0, len(ids)):
# 		if ids[x] == message.chat.id:
# 			answer[x] = ru
# 	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 	correct = random.randrange(0, 4, 1)
# 	incorrect = [-1, -1, -1, -1]
# 	t = 0
# 	while t != 4:
# 		n = random.randrange(0, len(words_d), 1)
# 		if n != task and incorrect.count(n) == 0:
# 			incorrect[t] = n
# 			t+=1
# 	# for x in incorrect:
# 	# 	print(x)
			
# 	it = [
# 	types.KeyboardButton(words_d[incorrect[0]][0]),
# 	types.KeyboardButton(words_d[incorrect[1]][0]),
# 	types.KeyboardButton(words_d[incorrect[2]][0]),
# 	types.KeyboardButton(words_d[incorrect[3]][0]),
# 	types.KeyboardButton("↩️ Назад")
# 	]
# 	it[correct] = types.KeyboardButton(ru)
# 	keyboard.add(it[0], it[1], it[2], it[3], it[4])
# 	bot.send_message(message.chat.id, eng, reply_markup=keyboard)

# 	filename = "./users/" + uname+".txt"
# 	myfile = open(filename, mode='w')
# 	pro_file = {
# 	'username': uname,
# 	'lvl': lvl,
# 	'xp': xp,
# 	'daily': daily,
# 	'education': education,
# 	'food': food,
# 	'wear': wear,
# 	'travel': travel,
# 	'reg': reg
# 	}
# 	json.dump(pro_file, myfile)
# 	myfile.close ()

def words_daily(message):
	global category
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			category[x] = 1
	global task
	task = random.randrange(0, len(words_d), 1)
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			while words_d[task][0] == answer[x]:
				task = random.randrange(0, len(words_d), 1)
	ru, eng = words_d[task]
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			answer[x] = ru
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	correct = random.randrange(0, 4, 1)
	incorrect = [-1, -1, -1, -1]
	t = 0
	while t != 4:
		n = random.randrange(0, len(words_d), 1)
		if n != task and incorrect.count(n) == 0:
			incorrect[t] = n
			t+=1
	# for x in incorrect:
	# 	print(x)
			
	it = [
	types.KeyboardButton(words_d[incorrect[0]][0]),
	types.KeyboardButton(words_d[incorrect[1]][0]),
	types.KeyboardButton(words_d[incorrect[2]][0]),
	types.KeyboardButton(words_d[incorrect[3]][0]),
	types.KeyboardButton("↩️ Назад")
	]
	it[correct] = types.KeyboardButton(ru)
	keyboard.add(it[0], it[1], it[2], it[3], it[4])
	bot.send_message(message.chat.id, eng, reply_markup=keyboard)

def words_education(message):
	global category
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			category[x] = 2
	global task
	task = random.randrange(0, len(words_e), 1)
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			while words_e[task][0] == answer[x]:
				task = random.randrange(0, len(words_e), 1)
	ru, eng = words_e[task]
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			answer[x] = ru
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	correct = random.randrange(0, 4, 1)
	incorrect = [-1, -1, -1, -1]
	t = 0
	while t != 4:
		n = random.randrange(0, len(words_e), 1)
		if n != task and incorrect.count(n) == 0:
			incorrect[t] = n
			t+=1
	# for x in incorrect:
	# 	print(x)
			
	it = [
	types.KeyboardButton(words_e[incorrect[0]][0]),
	types.KeyboardButton(words_e[incorrect[1]][0]),
	types.KeyboardButton(words_e[incorrect[2]][0]),
	types.KeyboardButton(words_e[incorrect[3]][0]),
	types.KeyboardButton("↩️ Назад")
	]
	it[correct] = types.KeyboardButton(ru)
	keyboard.add(it[0], it[1], it[2], it[3], it[4])
	bot.send_message(message.chat.id, eng, reply_markup=keyboard)

def words_food(message):
	global category
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			category[x] = 3
	global task
	task = random.randrange(0, len(words_f), 1)
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			while words_f[task][0] == answer[x]:
				task = random.randrange(0, len(words_f), 1)
	ru, eng = words_f[task]
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			answer[x] = ru
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	correct = random.randrange(0, 4, 1)
	incorrect = [-1, -1, -1, -1]
	t = 0
	while t != 4:
		n = random.randrange(0, len(words_f), 1)
		if n != task and incorrect.count(n) == 0:
			incorrect[t] = n
			t+=1
	# for x in incorrect:
	# 	print(x)
			
	it = [
	types.KeyboardButton(words_f[incorrect[0]][0]),
	types.KeyboardButton(words_f[incorrect[1]][0]),
	types.KeyboardButton(words_f[incorrect[2]][0]),
	types.KeyboardButton(words_f[incorrect[3]][0]),
	types.KeyboardButton("↩️ Назад")
	]
	it[correct] = types.KeyboardButton(ru)
	keyboard.add(it[0], it[1], it[2], it[3], it[4])
	bot.send_message(message.chat.id, eng, reply_markup=keyboard)

def words_wear(message):
	global category
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			category[x] = 4
	global task
	task = random.randrange(0, len(words_w), 1)
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			while words_w[task][0] == answer[x]:
				task = random.randrange(0, len(words_w), 1)
	ru, eng = words_w[task]
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			answer[x] = ru
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	correct = random.randrange(0, 4, 1)
	incorrect = [-1, -1, -1, -1]
	t = 0
	while t != 4:
		n = random.randrange(0, len(words_w), 1)
		if n != task and incorrect.count(n) == 0:
			incorrect[t] = n
			t+=1
	# for x in incorrect:
	# 	print(x)
			
	it = [
	types.KeyboardButton(words_w[incorrect[0]][0]),
	types.KeyboardButton(words_w[incorrect[1]][0]),
	types.KeyboardButton(words_w[incorrect[2]][0]),
	types.KeyboardButton(words_w[incorrect[3]][0]),
	types.KeyboardButton("↩️ Назад")
	]
	it[correct] = types.KeyboardButton(ru)
	keyboard.add(it[0], it[1], it[2], it[3], it[4])
	bot.send_message(message.chat.id, eng, reply_markup=keyboard)

def words_travel(message):
	global category
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			category[x] = 5
	global task
	task = random.randrange(0, len(words_t), 1)
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			while words_t[task][0] == answer[x]:
				task = random.randrange(0, len(words_t), 1)
	ru, eng = words_t[task]
	for x in range(0, len(ids)):
		if ids[x] == message.chat.id:
			answer[x] = ru
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	correct = random.randrange(0, 4, 1)
	incorrect = [-1, -1, -1, -1]
	t = 0
	while t != 4:
		n = random.randrange(0, len(words_t), 1)
		if n != task and incorrect.count(n) == 0:
			incorrect[t] = n
			t+=1
	# for x in incorrect:
	# 	print(x)
			
	it = [
	types.KeyboardButton(words_t[incorrect[0]][0]),
	types.KeyboardButton(words_t[incorrect[1]][0]),
	types.KeyboardButton(words_t[incorrect[2]][0]),
	types.KeyboardButton(words_t[incorrect[3]][0]),
	types.KeyboardButton("↩️ Назад")
	]
	it[correct] = types.KeyboardButton(ru)
	keyboard.add(it[0], it[1], it[2], it[3], it[4])
	bot.send_message(message.chat.id, eng, reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def logic(message):
	if ids.count(message.chat.id) == 0:
		ids.append(message.chat.id)
		answer.append('')
		category.append(0)
	# for x in ids:
	# 	print(x)
	# for x in answer:
	# 	print(x)
	now = datetime.now()
	print('[' + datetime.strftime(datetime.now(), "%H:%M:%S") + ']' +message.chat.username + ': ' + message.text)
	# Урок
	if message.text == '📓 Урок':
		bot.send_message(message.chat.id, 'Пожалуйста, выберете тип урока:', reply_markup=lesson1)
	# Новые слова
	elif message.text == '📓 Новые слова':
		bot.send_message(message.chat.id, 'Пожалуйста, выберете тему:', reply_markup=nwords)
	# Повседневные новые
	elif message.text == '🚰 Повседневные':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
		# newdaily(message)
	# Образование новые
	elif message.text == '📖 Образование':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# Еда новые
	elif message.text == '🍜 Еда':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# Одежда новые
	elif message.text == '👕 Одежда':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# Путешествия новые
	elif message.text == '🚢 Путешествия':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# Тест
	elif message.text == '📗        Тесты':
		bot.send_message(message.chat.id, 'Пожалуйста, выберете тему:', reply_markup=test)
	# 👋 Повседневные Тесты
	elif message.text == '👋 Повседневные':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# 📚 Образование Тесты
	elif message.text == '📚 Образование':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# 🍟 Еда Тесты
	elif message.text == '🍟 Еда':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# 👗 Одежда Тесты
	elif message.text == '👗 Одежда':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# 🌴 Путешествия Тесты
	elif message.text == '🌴 Путешествия':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# Повторение
	elif message.text == '📕 Повторение':
		bot.send_message(message.chat.id, 'В этом разделе вам будут предлагаться слова, а вы должны будете указать их перевод (у вас есть неограниченое количество попыток, за каждый правильный ответ вы будете получать 1 очко опыта)')
		bot.send_message(message.chat.id, 'Пожалуйста, выберете тему:', reply_markup=lesson)
	# Повседневные
	elif message.text == '🛁 Повседневные':
		words_daily(message)
	# Образование
	elif message.text == '📕 Образование':
		words_education(message)
	# Еда
	elif message.text == '🍔 Еда':
		words_food(message)
	# Одежда
	elif message.text == '👔 Одежда':
		words_wear(message)
	# Путешествия
	elif message.text == '✈ Путешествия':
		words_travel(message)
	# Кнопка назад
	elif message.text == '🔙 Назад':
		for x in range(0, len(ids)):
			if ids[x] == message.chat.id:
				category[x] = 0
		bot.send_message(message.chat.id, 'Хорошо, вот меню:', reply_markup=markup)
	elif message.text == '↩️ Назад':
		for x in range(0, len(ids)):
			if ids[x] == message.chat.id:
				category[x] = 0
		bot.send_message(message.chat.id, 'Хорошо, вот меню:', reply_markup=lesson1)
	# Игра
	elif message.text == '📒 Игра':
		bot.send_message(message.chat.id, 'Выберете что вас интересует:', reply_markup=game)
	# 
	elif message.text == '🎮 Игра':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	#
	elif message.text == '🏅 Рейтинг':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# Профиль
	elif message.text == '👤 Профиль':
		uname = message.chat.username
		filename = "./users/" + uname+".txt"
		myfile = open(filename, mode='r')
		jdata = json.load(myfile)
		admin = int(jdata['admin'])
		if admin >= 1:
			bot.send_message(message.chat.id, 'Введите имя пользователя:')
			for x in range(0, len(ids)):
				if ids[x] == message.chat.id:
					filename = message.text+".txt"
					myfile = open(filename, mode='r')
					jdata = json.load(myfile)
					full = str(int(jdata['daily'])+int(jdata['education'])+int(jdata['food'])+int(jdata['wear'])+int(jdata['travel']))
					bot.send_message(message.chat.id, '👤  Ваш ник: ' + str(jdata['username']) + '\n🥇 Ваш уровень: ' + str(jdata['lvl']) + ' (' + str(jdata['xp']) + '/50)' + '\n•  Изучено слов в теме: \n🛁 Повседневные:  ' + str(jdata['daily']) + '\n📕 Образование:  ' + str(jdata['education']) + '\n🍔 Еда:  ' + str(jdata['food']) + '\n👔 Одежда:  ' + str(jdata['wear']) + '\n✈ Путешествия:  ' + str(jdata['travel']) + '\n🏆 Всего слов изучено: ' + full)
		else:
			full = str(int(jdata['daily'])+int(jdata['education'])+int(jdata['food'])+int(jdata['wear'])+int(jdata['travel']))
			bot.send_message(message.chat.id, '👤  Ваш ник: ' + uname + '\n🥇 Ваш уровень: ' + str(jdata['lvl']) + ' (' + str(jdata['xp']) + '/50)' + '\n•  Изучено слов в теме: \n🛁 Повседневные:  ' + str(jdata['daily']) + '\n📕 Образование:  ' + str(jdata['education']) + '\n🍔 Еда:  ' + str(jdata['food']) + '\n👔 Одежда:  ' + str(jdata['wear']) + '\n✈ Путешествия:  ' + str(jdata['travel']) + '\n🏆 Всего слов изучено: ' + full)
		myfile.close ()	
	# Информация
	elif message.text == 'ℹ Информация':
		filename = "statistics.txt"
		myfile = open(filename, mode='r')
		jdata = json.load(myfile)
		regis = str(jdata['registered'])
		bot.send_message(message.chat.id, 'Количество регистрация: ' + regis + '\nСлов доступно: ' + words_str + '\nВерсия: ' + version + '\nРазработчики: @husak и @stefjen07\n')
	# Награды
	elif message.text == '🎖 Награды':
		bot.send_message(message.chat.id, '🛠 Раздел находится в разработке')
	# Пожертвования
	elif message.text == '💳 Пожертвовать':
		bot.send_message(message.chat.id, 'Вы можете материально поддержать моего бота. \nДеньги которые вы пожертвуете пойдут на улучшение и поддержание работы бота. \nНапример на оплату хостинга. \nВы можете пожертвовать деньги на развитие бота на эти счета WebMoney: \nZ280729802115 \nR739677431100 \nСпасибо вам большое :)')
	else:
		for x in range(0, len(ids)):
			if ids[x] == message.chat.id:
				if message.text == answer[x]:
					bot.send_message(message.chat.id, 'Верно 👍')
					uname = message.chat.username
					filename = "./users/" + uname+".txt"
					myfile = open(filename, mode='r')
					xpdata = json.load(myfile)
					xp_int = str(xpdata['xp'])
					xp_int_1 = int(xp_int) + 1
					global lvl_str
					lvl_int = str(xpdata['lvl'])
					lvl_str = str(lvl_int)
					global xp_str
					if xp_int_1 >= 50:
						lvl_str = str(int(lvl_int) + 1)
						xp_int_1 = 0
						bot.send_message(message.chat.id, '🏅 Поздравляем, вы повысили свой уровень до ' + lvl_str)
						print(message.chat.username + ' повысил свой уровень до ' + lvl_str)
					xp_str = str(xp_int_1)
					#тупо достаю переменные
					daily = str(xpdata['daily'])
					education = str(xpdata['education'])
					food = str(xpdata['food'])
					wear = str(xpdata['wear'])
					travel = str(xpdata['travel'])
					reg = str(xpdata['reg'])
					idu = str(xpdata['ID'])
					data = str(xpdata['data'])
					admin = str(xpdata['admin'])
					reward = str(xpdata['reward'])
					myfile.close ()
					filename = "./users/" + uname+".txt"
					myfile = open(filename, mode='w')
					pro_file = {
					'username': uname,
					'ID': idu,
					'data': data,
					'lvl': lvl_str,
					'xp': xp_str,
					'daily': daily,
					'education': education,
					'food': food,
					'wear': wear,
					'travel': travel,
					'reg': reg,
					'admin': admin,
					'reward': reward
					}
					json.dump(pro_file, myfile)
					myfile.close ()
					if category[x] == 1:
						words_daily(message)
					elif category[x] == 2:
						words_education(message)
					elif category[x] == 3:
						words_food(message)
					elif category[x] == 4:
						words_wear(message)
					elif category[x] == 5:
						words_travel(message)
					# elif category[x] == 6:
					# 	newdaily(message)
				elif category[x] != 0:
					bot.send_message(message.chat.id, 'Неверно 🔴')
				#Неизвестная команда
				else:
					bot.send_message(message.chat.id, 'Извините, но я не знаю эту команду 🤔', reply_markup=markup)

# RUN
bot.polling(none_stop=True)