import telebot
from telebot import types
from app import ask
from info import text_intro, info_for_role, termins_code, question_kr, oper_system
bot = telebot.TeleBot('YOUR_BOT_TOKEN')
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
markup_intro = types.InlineKeyboardButton('Преамбула')
markup_role = types.InlineKeyboardButton('Вопросы по Ролям')
markup_circle = types.InlineKeyboardButton('Вопросы по Кругу')
markup_termins = types.InlineKeyboardButton('Термины кодекса компании')
markup_op_sys_control = types.InlineKeyboardButton('Операционная система управления')
info = []

markup.add(markup_circle,markup_termins,markup_intro,markup_role, markup_op_sys_control)
@bot.message_handler(commands=['start'])
def start(message):
    text = f'Здравствуйте, {message.from_user.first_name}, я чат-бот компании  Smart Consulting,' \
           f' могу помочь с любым вопросом, касающимся кампании! Что вы хотите узнать?'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler()
def choice(message):
    match message.text.lower():
        case 'преамбула':
            info.append(text_intro)
            bot.send_message(message.chat.id, 'Задайте вопрос!')
        case 'термины кодекса компании':
            info.append(termins_code)
            bot.send_message(message.chat.id, 'Задайте вопрос!')
        case 'вопросы по ролям':
            info.append(info_for_role)
            bot.send_message(message.chat.id, 'Задайте вопрос!')
        case 'вопросы по кругу':
            info.append(question_kr)
            bot.send_message(message.chat.id, 'Задайте вопрос!')
        case 'операционная система управления':
            info.append(oper_system)
            bot.send_message(message.chat.id, 'Задайте вопрос!')
        case _:
            if info[-1] == '':
                bot.send_message(message.chat.id, 'Я вас не понял')
            else:
                text = ask(f'''Ответь на сообщение пользователя:
                Информация для ответа: {info[-1]}
                Сообщение пользователя: {message.text}''')
                bot.send_message(message.chat.id, text, reply_markup = markup)
bot.polling()