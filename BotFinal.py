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
    reclamo1 = types.InlineKeyboardButton(text="Producto defectuoso", callback_data="reclamo1")
    reclamo2 = types.InlineKeyboardButton(text="Problemas de entrega", callback_data="reclamo2")
    reclamo3 = types.InlineKeyboardButton(text="Producto incorrecto", callback_data="reclamo3")
    reclamo4 = types.InlineKeyboardButton(text="Problemas con el servicio al cliente", callback_data="reclamo4")
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    keyboard.add(reclamo1, reclamo2, reclamo3, reclamo4, back_button)
    bot.send_message(call.message.chat.id, "Estás en el flujo de Reclamos y quejas. \nElige una opción: \n1. Producto defectuoso \n2. Problemas de entrega \n3. Producto incorrecto \n4. Problemas con el servicio al cliente", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["reclamo1", "reclamo2", "reclamo3", "reclamo4"])
def reclamo_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    keyboard.add(back_button)
    if call.data == "reclamo1":
        bot.send_message(call.message.chat.id, "Producto defectuoso", reply_markup=keyboard)
    elif call.data == "reclamo2":
        bot.send_message(call.message.chat.id, "Problemas de entrega", reply_markup=keyboard)
    elif call.data == "reclamo3":
        bot.send_message(call.message.chat.id, "Producto incorrecto", reply_markup=keyboard)
    elif call.data == "reclamo4":
        bot.send_message(call.message.chat.id, "Problemas con el servicio al cliente", reply_markup=keyboard)


    

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
    producto1 = types.InlineKeyboardButton(text="Electrodomesticos", callback_data="producto1")
    producto2 = types.InlineKeyboardButton(text="Salud", callback_data="producto2")
    producto3 = types.InlineKeyboardButton(text="Libros", callback_data="producto3")
    producto4 = types.InlineKeyboardButton(text="Juguetes y juegos", callback_data="producto4")
    producto5 = types.InlineKeyboardButton(text="Deportes y Fitness", callback_data="producto5")
    producto6 = types.InlineKeyboardButton(text="Ropa", callback_data="producto6")
    keyboard.add(producto1)
    keyboard.add(producto2)
    keyboard.add(producto3)
    keyboard.add(producto4)
    keyboard.add(producto5)
    keyboard.add(producto6)
    keyboard.add(back_button)
    bot.send_message(call.message.chat.id, "Estás en el flujo de Nuestros productos. \nElige una opción: \n1.Electrodomesticos \n2. Salud\n3. Libros \n4. Juguetes y juegos\n 5. Deportes y Fitness \n 6. Ropa", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["producto1", "producto2", "producto3", "producto4", "producto5", "producto6"])
def reclamo_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text="Retroceder", callback_data="back")
    keyboard.add(back_button)
    if call.data == "producto1":
        bot.send_message(call.message.chat.id, "Has seleccionado Electrodomesticos")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto2":
        bot.send_message(call.message.chat.id, "Has seleccionado Salud.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto3":
        bot.send_message(call.message.chat.id, "Has seleccionado Libros.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto4":
        bot.send_message(call.message.chat.id, "Has seleccionado Juguetes y juegos.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto5":
        bot.send_message(call.message.chat.id, "Has seleccionado Deportes y Fitness.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))
    elif call.data == "producto6":
        bot.send_message(call.message.chat.id, "Has seleccionado Ropa.")
        bot.send_document(call.message.chat.id, open('PDF/Productos.pdf', 'rb'))


@bot.callback_query_handler(func=lambda call: call.data == "back")
def back_callback(call):
    send_welcome(call.message)

bot.polling()