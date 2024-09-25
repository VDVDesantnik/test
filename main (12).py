import telebot
from telebot import types
import random
import requests

bot = telebot.TeleBot('7372078127:AAFrqzkifOLyNp3JEVT50GxlB9-xTTtutAo')

with open('cats.txt', 'r', encoding='utf-8') as file:
    cats = file.readlines()
with open('dogs.txt', 'r', encoding='utf-8') as file:
    dogs = file.readlines()
with open('kapibara.txt', 'r', encoding='utf-8') as file:
    kapibara = file.readlines()

cat1 = open('Cats/веселый_кот.jpg', 'rb')
cat2 = open('Cats/довольный_кот.jpg', 'rb')
cat3 = open('Cats/забавный кот.jpg', 'rb')
cat4 = open('Cats/кот_в_ужасе.jpg', 'rb')
cat5 = open('Cats/крейзи_кот.jpg', 'rb')
cat6 = open('Cats/поддерживающий_кот.jpg', 'rb')
cat7 = open('Cats/поникший_кот.jpg', 'rb')
cat8 = open('Cats/расстроенный_кот.jpg', 'rb')
cat9 = open('Cats/удивленный_кот.jpg', 'rb')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'working!')


@bot.message_handler(commands=['info_animals'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Кошки', callback_data='cats_id')
    item2 = types.InlineKeyboardButton('Собаки', callback_data='dogs_id')
    item3 = types.InlineKeyboardButton('Капибары', callback_data='kapibara_id')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Приивет! О каком животном ты хочешь узнать интересный факт?',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    fact = ''
    if call.data == 'cats_id':
        fact = random.choice(cats)
    elif call.data == 'dogs_id':
        fact = random.choice(dogs)
    elif call.data == 'kapibara_id':
        fact = random.choice(kapibara)
    bot.send_message(call.message.chat.id, fact)


@bot.message_handler(commands=['cats_img'])
def button(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Весёлый кот')
    item2 = types.InlineKeyboardButton('Довольный кот')
    markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
    bot.send_message(message.chat.id, 'Выберите кота', reply_markup=markup)


@bot.message_handler()
def answer(message):
    if message.text == 'Довольный кот':
        bot.send_photo(message.chat.id, cat2)
    elif message.text == 'Весёлый кот':
        bot.send_photo(message.chat.id, cat1)
    elif message.text == 'Забавный кот':
        bot.send_photo(message.chat.id, cat3)
    elif message.text == 'Кот в ужасе':
        bot.send_photo(message.chat.id, cat4)
    elif message.text == 'Крейзи кот':
        bot.send_photo(message.chat.id, cat5)
    elif message.text == 'Поддерживающий кот':
        bot.send_photo(message.chat.id, cat6)
    elif message.text == 'Поникший кот':
        bot.send_photo(message.chat.id, cat7)
    elif message.text == 'Расстроенный кот':
        bot.send_photo(message.chat.id, cat8)
    elif message.text == 'Удивлённый кот':
        bot.send_photo(message.chat.id, cat9)


bot.polling(none_stop=True)
