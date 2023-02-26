import telebot
import config
from random import *
from telebot import types
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def Welcome(message):
    stik = open('welcome.webp','rb')
    bot.send_sticker(message.chat.id, stik)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число скажи!!!")
    item2 = types.KeyboardButton("Привет!")
    markup.add(item1,item2)
    bot.send_message(message.chat.id, "Привет, {0.first_name}.\nМеня зовут <b>{1.first_name}</b>, и я не бот.".format(message.from_user, bot.get_me()),parse_mode='html',reply_markup = markup)
    


@bot.message_handler(content_types = ['text'])
def say(message):
    if message.text == "Рандомное число скажи!!!":
        bot.send_message(message.chat.id, "Хорошо, хорошо, ваше число - {}".format(str(randint(0,100))))
    elif message.text.lower == "привет" or "привет!":
        bot.send_message(message.chat.id, "Пока")

bot.polling(none_stop = True)
