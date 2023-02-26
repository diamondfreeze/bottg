import telebot
import config
from random import *
from telebot import types
bot = telebot.TeleBot(config.TOKEN)
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
@bot.message_handler(commands=['start'])
def Welcome(message):
    stik = open('welcome.webp','rb')
    bot.send_sticker(message.chat.id, stik)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число скажи!!!")
    item2 = types.KeyboardButton("Привет!")
    item3 = types.KeyboardButton("Придумай пароль!")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Привет, {0.first_name}.\nМеня зовут <b>{1.first_name}</b>, и я не бот.".format(message.from_user, bot.get_me()),parse_mode='html',reply_markup = markup)
    


@bot.message_handler(content_types = ['text'])
def say(message):
    if message.text == "Рандомное число скажи!!!":
        bot.send_message(message.chat.id, "Хорошо, хорошо, ваше число - {}".format(randint(0,100)))
    elif message.text == "Привет!":
        bot.send_message(message.chat.id, "Пока!")
    elif message.text == "Придумай пароль!":
        bot.send_message(message.chat.id,"Ваш пароль {}.\nНикому его не говорите!!!".format(f"{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}"))

bot.polling(none_stop = True)
