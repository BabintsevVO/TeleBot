import telebot
from telebot import types

bot = telebot.TeleBot('5916308852:AAF2rIClnAD36dVXVo3i1eNqhMftVK5gRUE')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f"Hello, {message.from_user.first_name} <b>{message.from_user.first_name}</b>!"
    bot.send_message(message.chat.id, mess, parse_mode='html')

#  === Скроем, потому что забирает на себя команды по командам ниже ===
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text == 'hello':
#         bot.send_message(message.chat.id, f"И тебе привет!", parse_mode='html')
#     elif message.text == 'ID':
#         bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
#     else:
#         bot.send_message(message.chat.id, f"Команда не добавлена", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, f"Фото получено!", parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Enter website', url='www.google.com'))
    bot.send_message(message.chat.id, 'перейдите в гугл:', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    website = types.KeyboardButton('web site')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Выберите команду:', reply_markup=markup)


bot.polling(none_stop=True)
