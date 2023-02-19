# для постоянной работы
import os
import sys
from requests.exceptions import ConnectionError, ReadTimeout

# прочее
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import sqlite3

bot = telebot.TeleBot('6289501389:AAHDu3pA-MkEQzmZaQ2-oiesasxNiqZoSo4')


@bot.message_handler(commands=['start'])
def start(message):
    # создаем добавляем и клавиатуру
    markup = types.InlineKeyboardMarkup(row_width=1)
    item_1 = types.InlineKeyboardButton('Начать', callback_data='que1')

    markup.add(item_1)

    # подключаемся к БД
    connect = sqlite3.connect("data.db")
    cursor = connect.cursor()

    # записываем пользователя в бд
    id_ = [message.chat.id]
    cursor.execute("INSERT INTO progress(id) VALUES(?);", id_)
    connect.commit()

    # закрываем БД
    connect.close()

    bot.send_message(message.chat.id, "Добро пожаловать на викторину!", reply_markup=markup)


# обработчик Inline кнопок
@bot.callback_query_handler(func=lambda call: True)
def inline_handler_dude(call):
    if call.message:

        # вопрос 1
        if call.data == 'que1':
            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Масло', callback_data='correct')
            item_2 = types.InlineKeyboardButton('Масса', callback_data='miss')
            item_3 = types.InlineKeyboardButton('Масяня', callback_data='miss')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "От какого слова происходит название праздника Масленица?", reply_markup=markup)

        # вопрос 2
        if call.data == 'que2':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '2' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Бога Перуна', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Бога Урана', callback_data='miss')
            item_3 = types.InlineKeyboardButton('Бога Ярила', callback_data='correct')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "В честь какого бога празднуется Масленица?", reply_markup=markup)

        # вопрос 3
        if call.data == 'que3':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '3' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Холодец', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Блины', callback_data='correct')
            item_3 = types.InlineKeyboardButton('Щи', callback_data='miss')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "Какое блюдо обязательно готовят на Масленицу?", reply_markup=markup)

        # вопрос 4
        if call.data == 'que4':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '4' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Луны', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Марса', callback_data='miss')
            item_3 = types.InlineKeyboardButton('Солнца', callback_data='correct')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "Символом чего является блин?", reply_markup=markup)

        # вопрос 5
        if call.data == 'que5':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '5' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('скоморох', callback_data='correct')
            item_2 = types.InlineKeyboardButton('клоун', callback_data='miss')
            item_3 = types.InlineKeyboardButton('леший', callback_data='miss')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "Кто из этих персонажей связан с Масленицей?", reply_markup=markup)

        # вопрос 6
        if call.data == 'que6':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '6' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Среда', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Воскресенье', callback_data='correct')
            item_3 = types.InlineKeyboardButton('Пятница', callback_data='miss')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "В какой из дней Масленичной недели принято просить друг у друга прощение?", reply_markup=markup)

        # вопрос 7
        if call.data == 'que7':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '7' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Манную кашу', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Свиное сало', callback_data='miss')
            item_3 = types.InlineKeyboardButton('Гвоздику', callback_data='correct')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "Какой из этих компонентов никогда не добавляют в тесто для выпечки блинов?", reply_markup=markup)

        # вопрос 8
        if call.data == 'que8':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '8' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Лакомка', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Тёщины вечёрки', callback_data='correct')
            item_3 = types.InlineKeyboardButton('Широкий пир', callback_data='miss')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "Как называется пятый день Масленицы?", reply_markup=markup)

        # вопрос 9
        if call.data == 'que9':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '9' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Серебряную', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Хрустальную', callback_data='miss')
            item_3 = types.InlineKeyboardButton('Бриллиантовую', callback_data='correct')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "Какую Масленицу устроила царица Екатерина Великая в честь рождения внука?", reply_markup=markup)

        # вопрос 10
        if call.data == 'que10':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("UPDATE progress SET question = '10' WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            # создаем добавляем и клавиатуру
            markup = types.InlineKeyboardMarkup(row_width=1)
            item_1 = types.InlineKeyboardButton('Широкое гулянье', callback_data='miss')
            item_2 = types.InlineKeyboardButton('Прощеное воскресенье', callback_data='correct')
            item_3 = types.InlineKeyboardButton('Тёщины вечеринки', callback_data='miss')

            markup.add(item_1, item_2, item_3)

            bot.send_message(call.message.chat.id,
                             "Как называется последний день Масленицы?", reply_markup=markup)

        if call.data == 'miss':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("SELECT question FROM progress WHERE id = (?)", id_)
            question = cursor.fetchone()

            question_str = ""
            for i in question:
                question_str += str(i)
            question_int = int(question_str)

            question = str(question_int + 1)

            # закрываем БД
            connect.close()

            if question_int == 10:
                # создаем добавляем и клавиатуру
                markup = types.InlineKeyboardMarkup(row_width=1)
                item_1 = types.InlineKeyboardButton('Конец', callback_data='end')
                markup.add(item_1)

            else:
                # создаем добавляем и клавиатуру
                markup = types.InlineKeyboardMarkup(row_width=1)
                item_1 = types.InlineKeyboardButton('Следующий вопрос', callback_data=f'que{question}')
                markup.add(item_1)

            bot.send_message(call.message.chat.id,
                             "к сожалению, это неправильный ответ", reply_markup=markup)

        if call.data == 'correct':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("SELECT question FROM progress WHERE id = (?)", id_)
            question = cursor.fetchone()

            question_str = ""
            for i in question:
                question_str += str(i)
            question_int = int(question_str)

            question = str(question_int + 1)

            # закрываем БД
            connect.close()

            if question_int == 10:
                # создаем добавляем и клавиатуру
                markup = types.InlineKeyboardMarkup(row_width=1)
                item_1 = types.InlineKeyboardButton('Конец', callback_data='end')
                markup.add(item_1)

            else:
                # создаем добавляем и клавиатуру
                markup = types.InlineKeyboardMarkup(row_width=1)
                item_1 = types.InlineKeyboardButton('Следующий вопрос', callback_data=f'que{question}')
                markup.add(item_1)

            bot.send_message(call.message.chat.id,
                             "Это правильный ответ!", reply_markup=markup)

        if call.data == 'end':

            # подключаемся к БД
            connect = sqlite3.connect("data.db")
            cursor = connect.cursor()

            # выборка номера вопроса
            id_ = [call.message.chat.id]
            cursor.execute("DELETE FROM progress WHERE id = (?)", id_)
            connect.commit()

            # закрываем БД
            connect.close()

            bot.send_message(call.message.chat.id, "Спасибо за участие в викторине, вы молодцы!")
            bot.send_message(call.message.chat.id, "Если хотите сыграть еще раз, напишите /start")


# для постоянной работы
try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except (ConnectionError, ReadTimeout) as e:
    sys.stdout.flush()
    os.execv(sys.argv[0], sys.argv)
else:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
