# import telebot
# from telebot import types
#
# bot = telebot.TeleBot('7372078127:AAFrqzkifOLyNp3JEVT50GxlB9-xTTtutAo')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, 'working!')
#
#
# name = 'Капибара'
# energy = 70
# satiety = 10
# happiness = 100
#
#
# def feed():
#     global satiety, energy
#     satiety += 10
#     energy += 5
#
#
# def play():
#     global satiety, happiness, energy
#     satiety -= 5
#     energy -= 10
#     happiness += 10
#
#
# def sleep():
#     global satiety, happiness, energy
#     satiety -= 5
#     happiness -= 5
#     energy = 70
#
#
# @bot.message_handler(commands=['info'])
# def info_handler(message):
#     bot.send_message(message.chat.id,
#                      f'{name}\nУровень сытости: {satiety}\nУровень энергии: {energy}\nУровень счастья: {happiness}')
#
#
# @bot.message_handler(commands=['feed'])
# def feed_handler(message):
#     feed()
#     text = check()
#     bot.send_message(message.chat.id, f'{name} покушал\n{text}')
#
#
# @bot.message_handler(commands=['sleep'])
# def sleep_handler(message):
#     sleep()
#     text = check()
#     bot.send_message(message.chat.id, f'{name} поcпал\n{text}')
#
#
# @bot.message_handler(commands=['play'])
# def play_handler(message):
#     play()
#     text = check()
#     bot.send_message(message.chat.id, f'{name} поиграл\n{text}')
#
#
# @bot.message_handler(commands=['test_photo'])
# def send_photo(message):
#     bot.send_photo(message.chat.id, 'https://i.pinimg.com/originals/5b/6e/ca/5b6eca63605bea0eeb48db43f77fa0ce.jpg', caption='')
#
#
# def check():
#     global satiety, energy, happiness
#
#     if satiety <= 0:
#         return f'{name} умер от голода'
#     elif satiety < 20:
#         return f'{name} хочет кушать!'
#     elif satiety >= 20:
#         return f'{name} наелся и счастлив'
#     if happiness < 0:
#         return f'{name} умер от тоски. С питомцем надо чаще играть'
#     elif happiness > 100:
#         return f'{name} счастлив как никогда!'
#     if energy < 0:
#         return f'{name} умер от истощения'
#     elif energy < 15:
#         return f'{name} хочет спать'
#     else:
#         return f'{name} полон сил и энергии'
#
#
# bot.polling(none_stop=True)


import telebot
from telebot import types

bot = telebot.TeleBot('7372078127:AAFrqzkifOLyNp3JEVT50GxlB9-xTTtutAo')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'working!')


name = 'Капибара'
energy = 70
satiety = 10
happiness = 100


def feed():
    global satiety, energy
    satiety += 20
    energy += 5


def play():
    global satiety, happiness, energy
    satiety -= 5
    energy -= 10
    happiness += 10


def sleep():
    global satiety, happiness, energy
    satiety -= 5
    happiness -= 5
    energy = 70


@bot.message_handler(commands=['info'])
def info_handler(message):    bot.send_message(message.chat.id,
                                               f'{name}\nУровень сытости: {satiety}\nУровень энергии: {energy}\nУровень счастья: {happiness}')


@bot.message_handler(commands=['food'])
def feed_handler(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('водные растения', callback_data='fish_id')
    item2 = types.InlineKeyboardButton('клубни', callback_data='kot_id')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, 'Какую еду вы хотите выбрать?', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        feed()
        text = check()
        if call.data == 'fish_id':
            bot.send_photo(message.chat.id, 'https://cs14.pikabu.ru/post_img/2022/06/30/7/1656590277157171303.jpg',
                           caption=f'{name} покушал водных растений\n{text}')
        if call.data == 'kot_id':
            bot.send_photo(message.chat.id, 'https://cs14.pikabu.ru/post_img/2022/06/30/7/1656590277157171303.jpg',
                           caption=f'{name} покушал клубну\n{text}')


@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
    sleep()
    text = check()
    bot.send_photo(message.chat.id, 'https://minsknews.by/wp-content/uploads/2021/04/33979703.jpg',
                   caption=f'{name} поcпал\n{text}')


@bot.message_handler(commands=['play'])
def play_handler(message):
    play()
    text = check()
    if text == f'{name} наелся и счастлив':
        bot.send_photo(message.chat.id, 'https://cs14.pikabu.ru/post_img/2022/06/30/7/1656590277157171303.jpg',
                   caption=f'{name} поиграл\n{text}')
    else:
        bot.send_photo(message.chat.id, 'https://minsknews.by/wp-content/uploads/2021/04/33979703.jpg',
                   caption=f'{name} поиграл\n{text}')


@bot.message_handler()
def uncorrect(message):
    if message.text != '/info' and message.text != '/food' and message.text != '/sleep' and message.text != '/play':
        bot.send_message(message.chat.id,
                         'Данная команда не найденна, попробуйте /info либо /sleep либо /food либо /play либо /start')


def check():
    global satiety, energy, happiness
    if satiety <= 0:
        return f'{name} умер от голода'
    elif satiety < 20:
        return f'{name} хочет кушать!'
    elif satiety >= 20:
        return f'{name} наелся и счастлив'
    if happiness < 0:
        return f'{name} умер от тоски. С питомцем надо чаще играть'
    elif happiness > 100:
        return f'{name} счастлив как никогда!'
    if energy < 0:
        return f'{name} умер от истощения'
    elif energy < 15:
        return f'{name} хочет спать'
    else:
        return f'{name} полон сил и энергии'


bot.polling(none_stop=True)
