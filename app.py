# -*- coding: utf8 -*-

import time
import random
import urllib
from time import sleep
from io import BytesIO
from datetime import datetime

import telebot
import SimpleQIWI
from SimpleQIWI import *
from telebot import types

import menu
import config


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')

db.init_db()

bot = telebot.TeleBot(config.token, parse_mode=None)
api = QApi(token=config.token_qiwi, phone=config.qiwi)

print("Start")


all_users_file = open("all_users.txt", "r")
all_users = set()
for line in all_users_file:
	all_users.add(line.strip())
all_users_file.close()


def send_users(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.admin)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.admin)
			else:
				bot.send_message(config.admin_id, '✅ Рассылка была успешно отправлена!', reply_markup=menu.admin)
				for user in all_users:
					bot.send_message(user, message.text, reply_markup=menu.admin)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.admin)


def hello_edit(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.new_answer)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.new_answer)
			else:
				db.edit_settings_hel(message.text)
				bot.send_message(config.admin_id, '✅ Сохранено!\n\nДля корректной работы необходимо перезапустить бота.', reply_markup=menu.new_answer)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.new_answer)


def name_edit(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.admin)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.admin)
			else:
				file = open("name_shop.txt", "w")
				file.write(message.text)
				bot.send_message(config.admin_id, '✅ Сохранено!\n\nДля корректной работы необходимо перезапустить бота.', reply_markup=menu.admin)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.admin)


def qiwi_edit_number(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.payments)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.payments)
			else:
				file = open("qiwi_number.txt", "w")
				file.write(message.text)
				bot.send_message(config.admin_id, '✅ Сохранено!\n\nДля корректной работы необходимо перезапустить бота.', reply_markup=menu.payments)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.payments)


def edit_bitcoin(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.payments)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.payments)
			else:
				file = open("bitcoin.txt", "w")
				file.write(message.text)
				bot.send_message(config.admin_id, '✅ Сохранено!\n\nДля корректной работы необходимо перезапустить бота.', reply_markup=menu.payments)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.payments)


def qiwi_edit_token(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.payments)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.payments)
			else:
				file = open("qiwi_token.txt", "w")
				file.write(message.text)
				bot.send_message(config.admin_id, '✅ Сохранено!\n\nДля корректной работы необходимо перезапустить бота.', reply_markup=menu.payments)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.payments)


def info_edit(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.new_answer)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.new_answer)
			else:
				db.edit_settings_inf(message.text)
				bot.send_message(config.admin_id, '✅ Сохранено!\n\nДля корректной работы необходимо перезапустить бота.', reply_markup=menu.new_answer)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.new_answer)


def call_center(message):
	if message.chat.id == config.admin_id:
		try:
			if message.text == 'Отмена':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.new_answer)
			elif message.text == 'Вернуться':
				bot.send_message(config.admin_id, "Вы отменили действие", reply_markup=menu.new_answer)
			else:
				file = open("call_center_edit.txt", "w")
				file.write(message.text)
				bot.send_message(config.admin_id, '✅ Сохранено!\n\nДля корректной работы необходимо перезапустить бота.', reply_markup=menu.new_answer)
		except:
			bot.send_message(config.admin_id, "❌ Ошибка! Отправлять можно только текст.", reply_markup=menu.new_answer)


@bot.message_handler(commands=["start"])
def send_welcome(message):
	if not str(message.chat.id) in all_users:
		first_name = message.from_user.first_name
		last_name = message.from_user.last_name
		user_id = message.from_user.id
		today = datetime.datetime.today()
		date = today.strftime("%Y-%m-%d")
		db.add_user(first_name, last_name, date, user_id)
		logging.info("Bot was launched. ID: "+str(message.chat.id))
		all_users_file = open("all_users.txt", "a")
		all_users_file.write(str(message.chat.id) + "\n")
		all_users.add(str(message.chat.id))
		bot.send_message(message.chat.id, "{}\n\n{}".format(config.name, config.hello_text), reply_markup=menu.operator)
		#bot.send_message(message.chat.id, ""+config.name+"\n\nДобро пожаловать "+message.chat.first_name+"!\n\n♦️Вы можете совершить покупку и получить свой товар сразу после оплаты.\n♦️Выдача адресов круглосуточно без участия оператора!\n♦️Все безопасно и анонимно\n\n❗️Если возникнут какие-то проблемы - @admin", reply_markup=menu.operator)
		bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=menu.start)
	elif message.chat.id == config.admin_id:
		logging.info("Admin logged in bot. ID: "+str(message.chat.id))
		bot.send_message(config.admin_id, ""+config.name+"\n\nДобро пожаловать Администратор!\n\n♦️Вы можете совершить покупку и получить свой товар сразу после оплаты.\n♦️Выдача адресов круглосуточно без участия оператора!\n♦️Все безопасно и анонимно\n\n❗️Если возникнут какие-то проблемы - @admin", reply_markup=menu.operator)
		bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=menu.start2)
	else:
		logging.info("Bot was launched. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, "{}\n\n{}".format(config.name, config.hello_text), reply_markup=menu.operator)
		#bot.send_message(message.chat.id, ""+config.name+"\n\nДобро пожаловать "+message.chat.first_name+"!\n\n♦️Вы можете совершить покупку и получить свой товар сразу после оплаты.\n♦️Выдача адресов круглосуточно без участия оператора!\n♦️Все безопасно и анонимно\n\n❗️Если возникнут какие-то проблемы - @admin", reply_markup=menu.operator)
		bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=menu.start)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		if call.data == 'Проверить оплату':
			global order
			qiwiopl = random.randint(1, 4)
			btcopl = random.randint(1, 4)
			paypalopl = random.randint(1, 4)
			bot.send_message(call.message.chat.id, "⏳ Проверка оплаты..")
			time.sleep(qiwiopl)
			bot.send_message(call.message.chat.id, "❌ Оплата не найдена.")


@bot.message_handler(content_types=["text"])
def send_otziv(message):
	if message.text == '📦 Покупки':
		if message.chat.id == config.admin_id:
			logging.info("The admin clicked purchases. ID: "+str(message.chat.id))
			bot.send_message(message.chat.id, '❌ Покупки отсутствуют ❌')
		else:
			logging.info("The user clicked purchases. ID: "+str(message.chat.id))
			bot.send_message(message.chat.id, '❌ Покупки отсутствуют ❌')
	elif message.text == '💰Баланс':
		if message.chat.id == config.admin_id:
			try:
				api = QApi(token=config.token_qiwi, phone=config.qiwi)
				balance = api.balance[0]
				bot.send_message(config.admin_id, "🥝 Баланс вашего Киви: *"+str(balance)+"* руб", parse_mode='Markdown')
			except:
				bot.send_message(config.admin_id, "Ошибка!")
	elif message.text == '📈 Статистика':
		if message.chat.id == config.admin_id:
			users = db.return_users()
			buyers = db.return_buyers()
			sales = db.return_sales()
			bot.send_message(config.admin_id, '<a>📈 Статистика\n\n👨‍💻Кол-во пользователей: <b>{}</b>\n✅ Количество продаж: <b>{}</b>\n🧨Покупатели: <b>{}</b></a>'.format(users[0], sales[0], buyers[0]), parse_mode='HTML', reply_markup=menu.admin)
	elif message.text == 'Админ-Панель':
		if message.chat.id == config.admin_id:
			bot.send_message(config.admin_id, "☎️ Админ панель", reply_markup=menu.admin)
	elif message.text == '💶 Платёжки':
		if message.chat.id == config.admin_id:
			bot.send_message(config.admin_id, "Здесь Вы можете настроить и обновить Ваши платёжные данные.", reply_markup=menu.payments)
	elif message.text == 'Настройка Qiwi':
		if message.chat.id == config.admin_id:
			bot.send_message(config.admin_id, "Настройка Qiwi кошелька", reply_markup=menu.qiwi_edit)
	elif message.text == 'Настройка Bitcoin':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "Введите новый адрес bitcoin-кошелька: ", reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, edit_bitcoin)
	elif message.text == 'Выгрузка данных':
		if message.chat.id == config.admin_id:
			text_1 = '🧨 Данные платежных систем🧨'
			file_1 = open("qiwi_number.txt", "r")
			file_2 = open("qiwi_token.txt", "r")
			file_3 = open("bitcoin.txt", "r")
			text_2 = file_1.read()
			text_3 = file_2.read()
			text_4 = file_3.read()
			bot.send_message(config.admin_id, '<a><b>{}\n\n🥝 QIWI:\nНомер:</b> {}\n<b>Токен:</b> {}\n\n<b>💰BITCOIN:\nАдрес:</b> {}</a>'.format(text_1, text_2, text_3, text_4), parse_mode='HTML')
	elif message.text == '📲 Настройка ответов':
		if message.chat.id == config.admin_id:
			bot.send_message(config.admin_id, "В этом разделе вы можете полностью настроить и отредактировать информационный отдел.", reply_markup=menu.new_answer)
	elif message.text == '📩 Рассылка':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "Для отправки сообщения необходимо ввести текст:", reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, send_users)
	elif message.text == 'Изменить приветствие пользователя':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "<a>Отправьте мне сообщение, которое будет присылаться пользователю на команду start.\n\n<i>Внимание! Текст будет отображаться только для обычных пользователей, для админа он останется неизменным.</i></a>", parse_mode='HTML', reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, hello_edit)
	elif message.text == 'Добавить ответ на кнопку информация':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "Отправьте мне сообщение, которое будет присылаться при нажатии на кнопку.", reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, info_edit)
	elif message.text == '🖌 Название магазина':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "Введите название магазина: ", reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, name_edit)
	elif message.text == 'Изменить номер':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "Введите новый номер qiwi-кошелька: ", reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, qiwi_edit_number)
	elif message.text == 'Изменить токен':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "Введите новый токен qiwi-кошелька: ", reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, qiwi_edit_token)
	elif message.text == 'Редактирование отдела тех.поддержки':
		if message.chat.id == config.admin_id:
			msg = bot.send_message(config.admin_id, "Пришлите новый контакт для связи:\n\nПример - https://t.me/admin", reply_markup=menu.otmena)
			bot.register_next_step_handler(msg, call_center)
	elif message.text == 'Отправить новое сообщение':
		if message.chat.id == config.admin_id:
			bot.send_message(config.admin_id, "Начнем!\n\nВы можете отправить подписчикам одно или несколько сообщений, в том числе любые файлы, музыку,картинки и т.д\n\nДля того, чтобы сделать рассылку нажмите /send и введите ваше сообщение.", reply_markup=menu.krekin)
	elif message.text == '👤 Мой кабинет':
		if message.chat.id == config.admin_id:
			logging.info("The admin clicked office. ID: "+str(message.chat.id))
			bot.send_message(message.chat.id, "Информация об аккаунте\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💎 Никнейм: "+message.chat.username+"\n💎 Ваш ID: "+str(message.chat.id)+"\n💎 Кэшбек: 0 руб\n💎 Язык: Ru\n➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=menu.start2)
		else:
			logging.info("The user clicked office. ID: "+str(message.chat.id))
			bot.send_message(message.chat.id, "Информация об аккаунте\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n💎 Никнейм: "+message.chat.username+"\n💎 Ваш ID: "+str(message.chat.id)+"\n💎 Кэшбек: 0 руб\n💎 Язык: Ru\n➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=menu.start)
	elif message.text == '❔ Информация':
		if message.chat.id == config.admin_id:
			logging.info("The admin clicked info. ID: "+str(message.chat.id))
			bot.send_message(config.admin_id, config.information)
			#bot.send_message(message.chat.id, "Добро пожаловать!\n\n-------------------\nМы рады предложить Вам высококачественный товар, быстрый сервис обслуживания и доброжелательную атмосферу.\nУ нас Вы можете приобрести только лучшее качество товара по оптимальным ценам!\nДля постоянных клиентов - автоматическая система СКИДОК от 3-х покупок!\n\nОзнакомиться с бонусами и подарками можно здесь: http://hydrakxbeouow4af.onion/forum/thread/4371\n\n❗️Данный магазин является лишь демонстрацией разработчиков и их возможностей. Никакого отношения к ЦУМ Москва на сайте Hydra - ОН НЕ ИМЕЕТ. Подобные действия противозаконны. Деньги мы не принимаем и ничего не продаем!", reply_markup=menu.start2)
		else:
			bot.send_message(message.chat.id, config.information)
			logging.info("The user clicked info. ID: "+str(message.chat.id))
			#bot.send_message(message.chat.id, "Добро пожаловать!\n\n-------------------\nМы рады предложить Вам высококачественный товар, быстрый сервис обслуживания и доброжелательную атмосферу.\nУ нас Вы можете приобрести только лучшее качество товара по оптимальным ценам!\nДля постоянных клиентов - автоматическая система СКИДОК от 3-х покупок!\n\nОзнакомиться с бонусами и подарками можно здесь: http://hydrakxbeouow4af.onion/forum/thread/4371\n\n❗️Данный магазин является лишь демонстрацией разработчиков и их возможностей. Никакого отношения к ЦУМ Москва на сайте Hydra - ОН НЕ ИМЕЕТ. Подобные действия противозаконны. Деньги мы не принимаем и ничего не продаем!", reply_markup=menu.start)
	elif message.text == '🌿 Доступный ассортимент':
		logging.info("The user clicked items. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, "Выберите город:", reply_markup=menu.city)
	elif message.text == '🔙Назад':
		if message.chat.id == config.admin_id:
			bot.send_message(config.admin_id, '🔙Вы вернулись в главное меню', reply_markup=menu.start2)
		else:
			bot.send_message(message.chat.id, '🔙Вы вернулись в главное меню', reply_markup=menu.start)
	elif message.text == 'Москва':
		logging.info(str(message.from_user.first_name)+" chose the city of Moscow. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
	elif message.text == 'Санкт-Петербург':
		logging.info(str(message.from_user.first_name)+" chose the city of Saint Petersburg. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
	elif message.text == 'Екатеринбург':
		logging.info(str(message.from_user.first_name)+" chose the city of Yekaterinburg. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_ekb)
	elif message.text == 'Домодедово':
		logging.info(str(message.from_user.first_name)+" chose the city of Domodedovo. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
	elif message.text == 'Мытищи':
		logging.info(str(message.from_user.first_name)+" chose the city of Mytishchi. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
	elif message.text == 'Зеленоград':
		logging.info(str(message.from_user.first_name)+" chose the city of Zelenograd. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_perm)
	elif message.text == 'Подольск':
		logging.info(str(message.from_user.first_name)+" chose the city of Podolsk. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_voronezh)
	elif message.text == 'Челябинск':
		logging.info(str(message.from_user.first_name)+" chose the city of Chelyabinsk. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_voronezh)
	elif message.text == 'Нижний Новгород':
		logging.info(str(message.from_user.first_name)+" chose the city of Nizhny Novgorod. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
	elif message.text == 'Иркутск':
		logging.info(str(message.from_user.first_name)+" chose the city of Irkutsk. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
	elif message.text == 'Оренбург':
		logging.info(str(message.from_user.first_name)+" chose the city of Orenburg. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_perm)
	elif message.text == 'Пенза':
		logging.info(str(message.from_user.first_name)+" chose the city of Penza. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_spb)
	elif message.text == 'Омск':
		logging.info(str(message.from_user.first_name)+" chose the city of Omsk. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_voronezh)
	elif message.text == 'Пермь':
		logging.info(str(message.from_user.first_name)+" chose the city of Perm. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_perm)
	elif message.text == 'Рязань':
		plogging.info(str(message.from_user.first_name)+" chose the city of Ryazan. ID: "+str(message.chat.id))
		bot.send_message(message.chat.id, '⬇️ Какой район интересует? ⬇️', reply_markup=menu.rayon_msk)
	elif message.text in menu.rayon_spisok:
		logging.info(str(message.from_user.first_name) + ' chose the area ' + message.text + '. ID: ' + str(message.chat.id))
		assort = bot.send_message(message.chat.id, '🧨 Ассортимент 🧨', reply_markup=menu.what)
		bot.register_next_step_handler(assort, oplata)
	else:
		bot.send_message(message.chat.id, "Ничего не понятно!")


def oplata(message):
	global assort, tovarka
	tovarka = message.text
	if message.text in menu.what_spisok:
		comment = random.randint(10000, 99999)
		bot.send_message(message.chat.id, '⏳ Создаём заказ..')
		time.sleep(2)
		bot.send_message(message.chat.id, 'Информация об оплате\n➖➖➖➖➖➖➖➖➖➖\nТовар: '+tovarka+'\n\n💰 Оплата Bitcoin: '+config.bitcoin+'\n\n🥝 Оплата Qiwi: '+config.qiwi+'\n\n 📝 Комментарий к переводу: '+str(comment)+'\n➖➖➖➖➖➖➖➖➖➖\nПереводите ту сумму, на которую хотите пополнить баланс! Заполняйте номер телефона и комментарий при переводе внимательно!\n Администрация не несет ответственности за ошибочный перевод, возврата в данном случае не будет! После перевода нажмите кнопку Проверить оплату!', reply_markup=menu.keyboard)
		try:
			api.start()
			while True:
				if api.check(comment):
					date = datetime.datetime.now()
					today = datetime.datetime.today()
					date2 = today.strftime("%Y-%m-%d")
					print("New payment!")
					bot.send_message(config.admin_id, "<a><b>🎉 Пополнение!\n\nПользователь:</b> {}\n<b>Дата:</b> {}\n<b>Платёжка:</b> QIWI</a>".format(message.chat.id, date), parse_mode='HTML')
					db.add_buyer(message.chat.id, message.from_user.first_name)
					b.add_sale(message.chat.id, date2)
					purchase_old = db.return_user_sale(message.chat.id)
					purchase_new = int(purchase_old[0]) + 1
					db.add_sale_user(purchase_new, message.chat.id)
					break
				sleep(1)
			api.stop()
		except:
			logging.info("Error!")


#Запуск бота
if __name__ == '__main__':
	bot.polling(none_stop=True)
