# - *- coding: utf- 8 - *-

import telebot
from telebot import types

import config


rayon_spisok = ["🐊 ЦАО", "🐊 САО", "🐊 ВАО", "🐊 СВАО", "🐊 ЮВАО", "🐊 ЗАО", "🐊 ЮАО", "🐊 Выборгский район", "🐊 Московский район", "🐊 Петродворцовый район",
                "🐊 Курортный район", "🐊 Приморский район", "🐊 Пушкинский район", "🐊 Петроградский район", "🐊 Василеостровский район", "🐊 Красносельский район",
                "🐊 Невский район", "🐊 Верх-Исетский район", "🐊 Железнодорожный район", "🐊 Орджоникидзевский район", "🐊 Кировский район", "🐊 Октябрьский район",
                "🐊 Чкаловский район", "🐊 Ленинский район", "🐊 Центральный район", "🐊 Пролетарский район", "🐊 Зареченский район", "🐊 Привокзальный район",
                "🐊 Советский район", "🐊 Индустриальный район", "🐊 Европейский район", "🐊 МЖК", "🐊 Дом Обороны", "🐊 Ожогина", "🐊 Европейский район", "🐊 Восточный район",
                "🐊 Нижегородский район", "🐊 Приокский район", "🐊 Автозаводский район", "🐊 Канавинский район", "🐊 Сормовский район", "🐊 Куйбышевский район",
                "🐊 Самарский район", "🐊 Промышленный район", "🐊 Первомайский район", "🐊 Волжский район", "🐊 Заводской район", "🐊 Фрунзенский район",
                "🐊 ЦМР", "🐊 ФМР", "🐊 ЮМР", "🐊 ПМР", "🐊 СМР", "🐊 ЧМР", "🐊 МХГ", "🐊 КМР", "🐊 Коминтерновский район", "🐊 Левобережный район",
                "🐊 Приволжский район", "🐊 Ново-Савиновский район", "🐊 Вахитовский район", "🐊 Авиастроительный район", "🐊 Дзержинский район", "🐊 Мотовилихинский район"]


what_spisok = ["Товар 1", "Товар 2", "Товар 3", "Товар 4", "Товар 5"]


keyboard = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(
    text="Проверить оплату", callback_data="Проверить оплату")
keyboard.row(but_1)


what = types.ReplyKeyboardMarkup(True, False)
cocamq1 = types.KeyboardButton("Товар 1")
cocamq2 = types.KeyboardButton("Товар 1")
cocahq03 = types.KeyboardButton("Товар 1")
cocahq05 = types.KeyboardButton("Товар 1")
cocahq1 = types.KeyboardButton("Товар 1")
cocahq15 = types.KeyboardButton("Товар 1")
back = types.KeyboardButton("🔙Назад")
what.row(cocamq1)
what.row(cocamq2)
what.row(cocahq03)
what.row(cocahq05)
what.row(cocahq1)
what.row(cocahq15)
what.row(back)


otmena = telebot.types.ReplyKeyboardMarkup(True, False)
otmena.row("Отмена")
otmena.row("Вернуться")


start = telebot.types.ReplyKeyboardMarkup(True, False)
start.row('❔ Информация')
start.row('📦 Покупки', '👤 Мой кабинет')
start.row('🌿 Доступный ассортимент')


start2 = telebot.types.ReplyKeyboardMarkup(True, False)
start2.row('❔ Информация')
start2.row('📦 Покупки', '👤 Мой кабинет')
start2.row('🌿 Доступный ассортимент')
start2.row('Админ-Панель')


city = telebot.types.ReplyKeyboardMarkup(True, False)
city.row('Москва', 'Санкт-Петербург', 'Екатеринбург')
city.row('Домодедово', 'Мытищи', 'Зеленоград')
city.row('Подольск', 'Челябинск', 'Нижний Новгород')
city.row('Иркутск', 'Оренбург', 'Пенза')
city.row('Омск', 'Пермь', 'Рязань')
city.row('🔙Назад')


admin = telebot.types.ReplyKeyboardMarkup(True, False)
admin.row('💶 Платёжки', '🖌 Название магазина')
admin.row('📲 Настройка ответов', '📈 Статистика')
admin.row('📩 Рассылка', '💰Баланс')
admin.row('🔙Назад')


payments = telebot.types.ReplyKeyboardMarkup(True, False)
payments.row('Настройка Qiwi')
payments.row('Настройка Bitcoin')
payments.row('Выгрузка данных')
payments.row('🔙Назад')


qiwi_edit = telebot.types.ReplyKeyboardMarkup(True, False)
qiwi_edit.row('Изменить номер')
qiwi_edit.row('Изменить токен')
qiwi_edit.row('🔙Назад')


new_answer = telebot.types.ReplyKeyboardMarkup(True, False)
new_answer.row('Изменить приветствие пользователя')
new_answer.row('Добавить ответ на кнопку информация')
new_answer.row('Редактирование отдела тех.поддержки')
new_answer.row('🔙Назад')


krekin = telebot.types.ReplyKeyboardMarkup(True, False)
krekin.row('Отправить новое сообщение')
krekin.row('🔙Назад')


rayon_msk = types.ReplyKeyboardMarkup(True, False)
msk_cao = types.KeyboardButton("🐊 ЦАО")
msk_sao = types.KeyboardButton("🐊 САО")
msk_vao = types.KeyboardButton("🐊 ВАО")
msk_svao = types.KeyboardButton("🐊 СВАО")
msk_uvao = types.KeyboardButton("🐊 ЮВАО")
msk_zao = types.KeyboardButton("🐊 ЗАО")
msk_yao = types.KeyboardButton("🐊 ЮАО")
back = types.KeyboardButton("🔙Назад")
rayon_msk.row(msk_cao, msk_sao, msk_zao, msk_yao)
rayon_msk.row(msk_svao, msk_uvao)
rayon_msk.row(back)


rayon_spb = types.ReplyKeyboardMarkup(True, False)
spb_vib = types.KeyboardButton("🐊 Выборгский район")
spb_msk = types.KeyboardButton("🐊 Московский район")
spb_petrodvor = types.KeyboardButton("🐊 Петродворцовый район")
spb_kuror = types.KeyboardButton("🐊 Курортный район")
spb_prim = types.KeyboardButton("🐊 Приморский район")
spb_push = types.KeyboardButton("🐊 Пушкинский район")
spb_petrograd = types.KeyboardButton("🐊 Петроградский район")
spb_vas = types.KeyboardButton("🐊 Василеостровский район")
spb_krasn = types.KeyboardButton("🐊 Красносельский район")
spb_nevsk = types.KeyboardButton("🐊 Невский район")
back = types.KeyboardButton("🔙Назад")
rayon_spb.row(spb_vib, spb_msk)
rayon_spb.row(spb_petrodvor, spb_kuror)
rayon_spb.row(spb_prim, spb_push)
rayon_spb.row(spb_petrograd, spb_vas)
rayon_spb.row(spb_krasn, spb_nevsk)
rayon_spb.row(back)


rayon_ekb = types.ReplyKeyboardMarkup(True, False)
spb_verh = types.KeyboardButton("🐊 Верх-Исетский район")
spb_zhele = types.KeyboardButton("🐊 Железнодорожный район")
spb_ordzh = types.KeyboardButton("🐊 Орджоникидзевский район")
spb_oktyabr = types.KeyboardButton("🐊 Октябрьский район")
spb_chkal = types.KeyboardButton("🐊 Чкаловский район")
spb_lenin = types.KeyboardButton("🐊 Ленинский район")
spb_kirov = types.KeyboardButton("🐊 Кировский район")
back = types.KeyboardButton("🔙Назад")
rayon_ekb.row(spb_verh, spb_zhele)
rayon_ekb.row(spb_ordzh, spb_oktyabr)
rayon_ekb.row(spb_chkal, spb_lenin)
rayon_ekb.row(spb_kirov)
rayon_ekb.row(back)


rayon_voronezh = types.ReplyKeyboardMarkup(True, False)
voronezh_zhele = types.KeyboardButton("🐊 Железнодорожный район")
voronezh_centr = types.KeyboardButton("🐊 Центральный район")
voronezh_komin = types.KeyboardButton("🐊 Коминтерновский район")
voronezh_lenin = types.KeyboardButton("🐊 Ленинский район")
voronezh_sovet = types.KeyboardButton("🐊 Советский район")
voronezh_levober = types.KeyboardButton("🐊 Левобережный район")
back = types.KeyboardButton("🔙Назад")
rayon_voronezh.row(voronezh_zhele, voronezh_centr)
rayon_voronezh.row(voronezh_komin, voronezh_lenin)
rayon_voronezh.row(voronezh_sovet, voronezh_levober)
rayon_voronezh.row(back)


rayon_novosib = types.ReplyKeyboardMarkup(True, False)
navosib_zhele = types.KeyboardButton("🐊 Железнодорожный район")
navosib_zael = types.KeyboardButton("🐊 Заельцовский район")
navosib_kalin = types.KeyboardButton("🐊 Калининский район")
navosib_kirov = types.KeyboardButton("🐊 Кировский район")
navosib_oktyab = types.KeyboardButton("🐊 Октябрьский район")
navosib_lenin = types.KeyboardButton("🐊 Ленинский район")
navosib_pervo = types.KeyboardButton("🐊 Первомайский район")
navosib_sovet = types.KeyboardButton("🐊 Советский район")
back = types.KeyboardButton("🔙Назад")
rayon_novosib.row(navosib_zhele, navosib_zael)
rayon_novosib.row(navosib_kalin, navosib_kirov)
rayon_novosib.row(navosib_oktyab, navosib_lenin)
rayon_novosib.row(navosib_pervo, navosib_sovet)
rayon_novosib.row(back)


rayon_perm = types.ReplyKeyboardMarkup(True, False)
perm_dzer = types.KeyboardButton("🐊 Дзержинский район")
perm_indu = types.KeyboardButton("🐊 Индустриальный район")
perm_kirov = types.KeyboardButton("🐊 Кировский район")
perm_lenin = types.KeyboardButton("🐊 Ленинский район")
perm_motov = types.KeyboardButton("🐊 Мотовилихинский район")
back = types.KeyboardButton("🔙Назад")
rayon_perm.row(perm_dzer, perm_indu)
rayon_perm.row(perm_kirov, perm_lenin)
rayon_perm.row(perm_motov)
rayon_perm.row(back)


operator = types.InlineKeyboardMarkup()
but_1 = types.InlineKeyboardButton(text="Тех.Поддержка", url=config.support)
operator.row(but_1)
