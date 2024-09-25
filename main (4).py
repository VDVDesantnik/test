import telebot

with open('citles.txt', 'r', encoding='utf-8') as f:
    bot = telebot.TeleBot('7156648136:AAErCa3Qzjk6fJIr0_pl2MGPJ7zHm55yys4')


    @bot.message_handler(commands=['start'])
    def hello(message):
        bot.send_message(message.chat.id, 'Привет, это бот который играет в города, поиграем(Только Русские города)?')

    @bot.message_handler(commands=['Да', 'Давай', 'Можно', 'Не против'])
    def goroda(message):
        bot.send_message(message.chat.id, 'Я начну, ')




bot.polling(non_stop=True)