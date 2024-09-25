import telebot
from telebot import types
import time

bot = telebot.TeleBot('7156648136:AAErCa3Qzjk6fJIr0_pl2MGPJ7zHm55yys4')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'working!')


name = 'Капибара'
energy = 70
satiety = 10
happiness = 100
money = 0

def feed():
    global satiety, energy, money
    satiety += 20
    energy += 5
    money -= 3

def play():
    global satiety, happiness, energy
    satiety -= 5
    energy -= 10
    happiness += 10

def money1():
    global money
def sleep():
    global satiety, happiness, energy
    satiety -= 5
    happiness -= 5
    energy = 70


def jobss():
    global satiety, happiness, energy, money
    satiety -= 20
    happiness -= 20
    energy -= 30
    money += 100


@bot.message_handler(commands=['info'])
def info_handler(message):    bot.send_message(message.chat.id,
                                               f'{name}\nУровень сытости: {satiety}\nУровень энергии: {energy}\nУровень счастья: {happiness}')


@bot.message_handler(commands=['food'])
def food(message):
    feed()
    text = check()
    bot.send_message(message.chat.id, 'Капибара поел')


@bot.message_handler(commands=['house'])
def feed_handler(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('квартира', callback_data='dom')
    item2 = types.InlineKeyboardButton('загарадный дом', callback_data='housee')
    item3 = types.InlineKeyboardButton('У бабашки', callback_data='grandmother')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Какую еду вы хотите выбрать?', reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        global money
        feed()
        text = check()
        if call.data == 'dom':
            if money <= 250:
                money -= 250
                bot.send_photo(message.chat.id,
                               'https://avatars.mds.yandex.net/i?id=ee9937515d6132b39fa0c1f78c3de232_l-13288255-images-thumbs&n=13',
                               caption=f'{name} капибара переехал в новый домик😍\n{text}')
            else:
                bot.send_message(message.chat.id, 'У капибары нету денег( Заработай их через команду /jobs, проверить свои сбережения через /money!')
        if call.data == 'housee':
            if money <= 500:
                money -= 500
                bot.send_photo(message.chat.id,
                               'https://s14.stc.yc.kpcdn.net/share/i/12/13242595/wr-960.webp',
                               caption=f'{name} капибара переехал в новый домик😍\n{text}')
            else:
                bot.send_message(message.chat.id,
                             'У капибары нету денег( Заработай их через команду /jobs, проверить свои сбережения через /money!')
        if call.data == 'grandmother':
            if money <= 25:
                money -= 25
                bot.send_photo(message.chat.id, 'https://avatars.dzeninfra.ru/get-zen_doc/4450356/pub_62bfd3738891784cf0b94841_62bfd890ed0a440ad236a25c/scale_1200',
                               caption=f'{name} капибара переехал в новый домик😍\n{text}')
            else:
                bot.send_message(message.chat.id, 'У капибары нету денег( Заработай их через команду /jobs, проверить свои сбережения через /money!')


@bot.message_handler(commands=['sleep'])
def sleep_handler(message):
    sleep()
    text = check()
    bot.send_photo(message.chat.id, 'https://minsknews.by/wp-content/uploads/2021/04/33979703.jpg',
                   caption=f'{name} поcпал\n{text}')


@bot.message_handler(commands=['money'])
def moneyy(message):
    money1()
    bot.send_message(message.chat.id, f'Ваши деньги {money}')


@bot.message_handler(commands=['jobs'])
def jobs(message):
    if satiety >= 25 and happiness >= 25 and energy >= 35:
        jobss()
        # text = check()
        time.sleep(15)
        bot.send_message(message.chat.id, f'Капибара поработал у очень устал {money}')
    else:
        bot.send_message(message.chat.id, 'Капибара не можеьрабоать!')




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
    if message.text != '/info' and message.text != '/food' and message.text != '/sleep' and message.text != '/play' and message.text != '/jobs' and message.text != '/money':
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