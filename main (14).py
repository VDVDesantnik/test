import telebot
from telebot import types
import datetime

bot = telebot.TeleBot('7156648136:AAErCa3Qzjk6fJIr0_pl2MGPJ7zHm55yys4')

count = 0
true_answer_count = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'working!')

@bot.message_handler(commands=['birthday'])
def birthday(message):
    bot.send_message(message.chat.id, 'Введите дату вашего рождения в формате год-месяц-день')


@bot.message_handler()
def get_birthday(message):
    temp = message.text.split('-')
    temp = list(map(lambda x: int(x), temp))
    birthday = datetime.datetime(datetime.datetime.now().year, temp[1], temp[2])
    current_day = datetime.datetime.now()
    result = current_day - birthday
    bot.send_message(message.chat.id, f'{abs(result.days)}')




bot.polling(none_stop=True)
