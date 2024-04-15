import telebot 
from telebot import types

bot = telebot.TeleBot("6441365825:AAHWDtuHdobmZ0CR7Iu40BRi-SleD0_fpYg")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="types.InlineKeyboardButton 1", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="types.InlineKeyboardButton 2", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="types.InlineKeyboardButton 1", callback_data="button1")
    button4= types.InlineKeyboardButton(text="types.InlineKeyboardButton 2", callback_data="button2")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    keyboard.add(button4)
    bot.send_message(message.chat.id, "Hola, elige una opción:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "button1":
        bot.answer_callback_query(call.id, "Has pulsado el botón 1")
    elif call.data == "button2":
        bot.answer_callback_query(call.id, "Has pulsado el botón 2")

bot.polling()