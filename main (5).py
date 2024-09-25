import telebot
import random
import requests
import string


poke_api_url = 'https://pokeapi.co/api/v2/pokemon/'
bot = '7156648136:AAErCa3Qzjk6fJIr0_pl2MGPJ7zHm55yys4'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(commands=['pokemon'])
def send_poke_info(message):
    poke_id = random.randint(1,898)
    url = poke_api_url + str(poke_id)
    response = requests.get(url)
    data = response.json()
    if 'sprites' in data and 'front_default' in data['sprites']:
        poke_name = data['name'].capitalize()
        poke_img_url = data['sprites']['front_default']
        poke_info = f'{poke_id} {poke_name}\n'
        poke_info += 'Типы: '



bot.polling(none_stop=True)