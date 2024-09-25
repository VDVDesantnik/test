import telebot
import random

# 7372078127:AAFrqzkifOLyNp3JEVT50GxlB9-xTTtutAo

file = open('photo_2024.jpg', 'rb')
bot = telebot.TeleBot('7372078127:AAFrqzkifOLyNp3JEVT50GxlB9-xTTtutAo')

s = ['камень', 'ножницы', 'бумага']


def config_func(user_answer, bot_answer):
    if user_answer == 'камень' and bot_answer == 'камень':
        return 'ничья'
    elif user_answer == 'камень' and bot_answer == 'ножницы':
        return 'ты победил'
    elif user_answer == 'камень' and bot_answer == 'бумага':
        return 'повезёт в следующий раз'
    elif user_answer == 'ножницы' and bot_answer == 'ножницы':
        return 'ничья'
    elif user_answer == 'ножницы' and bot_answer == 'бумага':
        return 'ты победил'
    elif user_answer == 'ножницы' and bot_answer == 'камень':
        return 'повезёт в следующий раз'
    elif user_answer == 'бумага' and bot_answer == 'бумага':
        return 'ничья'
    elif user_answer == 'бумага' and bot_answer == 'камень':
        return 'ты победил'
    elif user_answer == 'бумага' and bot_answer == 'ножницы':
        return 'повезёт в следующий раз'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler()
def play(message):
    user_answer = message.text.lower()
    bot_answer = random.choice(s)
    res = config_func(user_answer, bot_answer)
    bot.send_message(message.chat.id, f'Ответ бота: {bot_answer}\nИтог: {res}')


# @bot.message_handler(func=lambda message: message.text.lower() == 'привет')
# def myTest(message):
#     bot.send_message(message.chat.id, 'Привет!!!')
#
#
# @bot.message_handler(func=lambda message: True)
# def f(message):
#     bot.reply_to(message, message.text)


bot.polling(none_stop=True)
