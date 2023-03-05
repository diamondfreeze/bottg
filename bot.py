import telebot
from telebot import types
import configtok
import countries
import stories
from random import *
from time import sleep

mode = 'standart'
bot = telebot.TeleBot(configtok.TOKEN)
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']





@bot.message_handler(commands=['start'])
def welcome(message):
    stik = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, stik)
    welcome_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    welcome_item1 = types.KeyboardButton("Привет!!!")
    welcome_markup.add(welcome_item1)
    bot.send_message(message.chat.id,
                     'Привет, {0.first_name}.\n'
                     'Меня зовут <b>{1.first_name}</b>.\n'
                     'Поздоровайся со мной!!!'.format(message.from_user, bot.get_me()),
                     parse_mode='html',
                     reply_markup=welcome_markup,
                     )


@bot.message_handler(content_types=['text'])
def say(message):
    global mode
    if mode != 'active_bomber':
        if message.text == "Привет!!!" or message.text == "Назад":
            mode = 'standart'
            bass_markup = types.ReplyKeyboardMarkup(row_width=2,
                                                    resize_keyboard=True,
                                                    )
            bass_item1 = types.KeyboardButton("Рандомный режим")
            bass_item2 = types.KeyboardButton("Кинуть бомбер")
            bass_item3 = types.KeyboardButton("Расскажи мне историю")
            bass_item4 = types.KeyboardButton("Давай играть в столицы")
            bass_markup.add(bass_item1, bass_item2, bass_item3, bass_item4)
            bot.send_message(message.chat.id,
                             "Привет, {0.first_name}!!!".format(message.from_user),
                             parse_mode='html',
                             reply_markup=bass_markup,
                             )

        # randommode
        elif message.text == "Рандомный режим" and mode == 'standart':
            mode = 'random'
            random_markup = types.ReplyKeyboardMarkup(row_width=2,
                                                      resize_keyboard=True,
                                                      )
            random_item1 = types.KeyboardButton("Скажи рандом число")
            random_item2 = types.KeyboardButton("Придумай пароль")
            random_item3 = types.KeyboardButton("Назад")
            random_markup.add(random_item1, random_item2, random_item3)
            bot.send_message(message.chat.id,
                             "RANDOM MODE ACTIVATED",
                             parse_mode='html',
                             reply_markup=random_markup,
                             )

        elif message.text == "Скажи рандом число" and mode == 'random':
            bot.send_message(message.chat.id,
                             "Хорошо, хорошо, ваше число - {}".format(randint(0, 10000)))

        elif message.text == "Придумай пароль" and mode == 'random':
            bot.send_message(message.chat.id, "Ваш пароль {}\nНикому его не говорите\nЯ итак уже всем скинул".format(
                f"{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}{choice(alpha)}"))

        # bombermode
        elif message.text == "Кинуть бомбер" and mode == 'standart':
            mode = 'bomber'
            bomber_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bomber_item1 = types.KeyboardButton('Назад')
            bomber_markup.add(bomber_item1)
            bot.send_message(message.chat.id, "Введите номер телефона жертвы.\nПример:8 987-654-32-10",
                             parse_mode='html',
                             reply_markup=bomber_markup,
                             )

        elif message.text != 'Назад' and mode == 'bomber':
            mode = 'active_bomber'
            clear_markup = types.ReplyKeyboardMarkup(row_width=2,
                                                     resize_keyboard=True,
                                                     )
            clear = types.KeyboardButton(f"{choice(['Пожалуйста, остановись', 'Пощади!', 'NO, GOD, NOO!'])}")
            clear_markup.add(clear)
            bot.send_message(message.chat.id,
                             "Кидать бомберы плохо, поэтому получай!",
                             parse_mode='html',
                             reply_markup=clear_markup)
            clear_markup = types.ReplyKeyboardRemove()
            bomber_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bomber_item1 = types.KeyboardButton("Назад")
            bomber_markup.add(bomber_item1)
            sleep(3)

            for i in range(50):
                bot.send_message(message.chat.id,
                                 f"{choice(['Так делать нельзя!', 'Ты понял, что нельзя кидать бомберы?', 'В следующий раз не кидай бомберы!'])}")

            mode = 'standart'
            bot.send_message(message.chat.id,
                             '\nНадеюсь ты выучил урок!',
                             parse_mode='html',
                             reply_markup=bomber_markup,
                             )

        # storymode
        elif message.text == 'Расскажи мне историю' or message.text == 'Расскажи ещё одну историю!':
            mode = 'story'
            story_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            story_item1 = types.KeyboardButton('Назад')
            story_item2 = types.KeyboardButton('Расскажи ещё одну историю!')
            story_markup.add(story_item1, story_item2)
            bot.send_message(message.chat.id,
                             choice(stories.stories),
                             parse_mode='html',
                             reply_markup=story_markup,
                             )
            mode = 'standart'
        #ctolicamode
        elif message.text == 'Давай играть в столицы':
            mode = 'ctolica'
            strana = []
            ctolica_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            materic = choice([countries.euro_jopa, countries.asia_jopa, countries.south_jopa, countries.north_jopa, countries.avstralia_jopa])
            for keys in materic:
                strana.append(keys)
            strana = choice(strana)
            materichok = choice([countries.euro_jopa, countries.asia_jopa, countries.south_jopa, countries.north_jopa, countries.avstralia_jopa])
            print(choice([s for s in materichok]))
            ctolica_item1 = types.KeyboardButton(f'{materic[strana]}')
            ctolica_markup.add(ctolica_item1)



        else:
            bot.send_message(message.chat.id,
                             'У меня нет такой функции\n'
                             'Обращайтесь к админам DiamondFreeze и NikitaPROGOD!')


bot.polling(none_stop=True)
