import telebot 
from telebot import types

bot = telebot.TeleBot("6441365825:AAHWDtuHdobmZ0CR7Iu40BRi-SleD0_fpYg")

def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Reclamos y quejas", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="Nuestros locales", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="Nuestros productos", callback_data="button3")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.send_message(message.chat.id, "Hola, Soy Bot de Tienda_X, en que puedo ayudarte.\nElige una opción:", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def start_message(message):
    send_welcome(message)

@bot.callback_query_handler(func=lambda call: call.data == "button1")
def button1_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    reclamo1 = types.InlineKeyboardButton(text="Reclamo 1", callback_data="reclamo1")
    reclamo2 = types.InlineKeyboardButton(text="Reclamo 2", callback_data="reclamo2")
    reclamo3 = types.InlineKeyboardButton(text="Reclamo 3", callback_data="reclamo3")
    reclamo4 = types.InlineKeyboardButton(text="Reclamo 4", callback_data="reclamo4")
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    keyboard.add(reclamo1, reclamo2, reclamo3, reclamo4, back_button)
    bot.send_message(call.message.chat.id, "Estás en el flujo de Reclamos y quejas. \nElige una opción: \n1.Esta la opción del reclamo 1 \n2.Esta la opción del reclamo 2 \n3.Esta la opción del reclamo 3 \n4.Esta la opción del reclamo 4", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["reclamo1", "reclamo2", "reclamo3", "reclamo4"])
def reclamo_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    keyboard.add(back_button)
    if call.data == "reclamo1":
        bot.send_message(call.message.chat.id, "Has seleccionado el Reclamo 1. Aquí está la solución para el Reclamo 1.", reply_markup=keyboard)
    elif call.data == "reclamo2":
        bot.send_message(call.message.chat.id, "Has seleccionado el Reclamo 2. Aquí está la solución para el Reclamo 2.", reply_markup=keyboard)
    elif call.data == "reclamo3":
        bot.send_message(call.message.chat.id, "Has seleccionado el Reclamo 3. Aquí está la solución para el Reclamo 3.", reply_markup=keyboard)
    elif call.data == "reclamo4":
        bot.send_message(call.message.chat.id, "Has seleccionado el Reclamo 4. Aquí está la solución para el Reclamo 4.", reply_markup=keyboard)
    

@bot.callback_query_handler(func=lambda call: call.data == "button2")
def button2_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    keyboard.add(back_button)
    bot.send_message(call.message.chat.id, "Estás en el flujo de Nuestros locales. ¿Qué te gustaría hacer?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "button3")
def button3_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    producto1 = types.InlineKeyboardButton(text="Producto 1", callback_data="producto1")
    producto2 = types.InlineKeyboardButton(text="Producto 2", callback_data="producto2")
    producto3 = types.InlineKeyboardButton(text="Producto 3", callback_data="producto3")
    producto4 = types.InlineKeyboardButton(text="Producto 4", callback_data="producto4")
    producto5 = types.InlineKeyboardButton(text="Producto 5", callback_data="producto5")
    producto6 = types.InlineKeyboardButton(text="Producto 6", callback_data="producto6")
    keyboard.add(producto1)
    keyboard.add(producto2)
    keyboard.add(producto3)
    keyboard.add(producto4)
    keyboard.add(producto5)
    keyboard.add(producto6)
    keyboard.add(back_button)
    bot.send_message(call.message.chat.id, "Estás en el flujo de Nuestros productos. \nElige una opción: \n1.Esta la opción del Producto 1 \n2.Esta la opción del Producto 2 \n3.Esta la opción del Producto 3 \n4.Esta la opción del Producto 4 \n 5.Esta la opción del Producto 5 \n 6.Esta la opción del Producto 6 ", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["producto1", "producto2", "producto3", "producto4", "producto5", "producto6"])
def reclamo_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    keyboard.add(back_button)
    if call.data == "producto1":
        bot.send_message(call.message.chat.id, "Has seleccionado el Producto 1.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto2":
        bot.send_message(call.message.chat.id, "Has seleccionado el Producto 2.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto3":
        bot.send_message(call.message.chat.id, "Has seleccionado el Producto 3.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto4":
        bot.send_message(call.message.chat.id, "Has seleccionado el Producto 4.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto5":
        bot.send_message(call.message.chat.id, "Has seleccionado el Producto 5.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto6":
        bot.send_message(call.message.chat.id, "Has seleccionado el Producto 6.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))


@bot.callback_query_handler(func=lambda call: call.data == "back")
def back_callback(call):
    send_welcome(call.message)

bot.polling()