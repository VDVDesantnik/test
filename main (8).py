import telebot
import random

# 7372078127:AAFrqzkifOLyNp3JEVT50GxlB9-xTTtutAo


bot = telebot.TeleBot('7156648136:AAErCa3Qzjk6fJIr0_pl2MGPJ7zHm55yys4')

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



bot.polling(none_stop=True)
