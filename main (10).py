import telebot
import random
import requests

with open('pokeinfodfg.txt', 'w', encoding='utf-8') as f:
    bot = telebot.TeleBot('7156648136:AAErCa3Qzjk6fJIr0_pl2MGPJ7zHm55yys4')
    poke_api_url = "https://pokeapi.co/api/v2/pokemon/"

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Hello')


    @bot.message_handler(commands=['pokemon'])
    def send_poke_info(message):
        poke_id = random.randint(1, 898)
        url = poke_api_url + str(poke_id)
        response = requests.get(url)
        data = response.json()
        if 'sprites' in data and 'front_default' in data['sprites']:
            poke_name = data['name'].capitalize()
            poke_img_url = data['sprites']['front_default']
            poke_info = f'{poke_id} {poke_name}\n'
            poke_info += 'Типы: '
            for poke_type in data['types']:
                poke_info += f'{poke_type["type"]["name"]}'
            bot.send_photo(message.chat.id, poke_img_url, caption=poke_info)
        f.write(poke_info)

    @bot.message_handler()
    def send_poke_info_by_name(message):
        pokemon_name = message.text.lower()
        url = poke_api_url + pokemon_name
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            poke_name = data['name'].capitalize()
            poke_img_url = data['sprites']['front_default']
            poke_info = f'{poke_name}\n'
            poke_info += 'Типы: '
            for poke_type in data['types']:
                poke_info += f'{poke_type["type"]["name"]}'
            bot.send_photo(message.chat.id, poke_img_url, caption=poke_info)
        else:
            bot.reply_to(message, f'Покемон с именем {pokemon_name} не найден')
        f.write(555)









    bot.polling(none_stop=True)