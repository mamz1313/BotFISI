import telebot 
from telebot import types

bot = telebot.TeleBot("6441365825:AAHWDtuHdobmZ0CR7Iu40BRi-SleD0_fpYg")

# Diccionario que mapea los códigos de los estudiantes a sus nombres
student_codes = {
    "19200171": "Vilchez Giraldo Jamie Edinso",
    "19200186": "Muñoz Zeballos Manuel Alejandro",
    "20200218": "Torres Espinoza Alejandro Paul",
    # Agrega aquí todos los códigos y nombres de estudiantes que necesites
}

# Diccionario que mapea los códigos de los estudiantes a sus cursos y salones
student_courses = {
    "19200171": {
        "Lunes": [("Curso 1", "Salón 101"), ("Curso 2", "Salón 102")],
        "Martes": [("Curso 3", "Salón 201")],
        # Agrega aquí todos los cursos y salones para cada día de la semana
    },
    "19200171": {
        "Lunes": [("Curso 4", "Salón 301"), ("Curso 5", "Salón 302")],
        "Martes": [("Curso 6", "Salón 401")],
        # Agrega aquí todos los cursos y salones para cada día de la semana
    },
    # Agrega aquí todos los códigos y cursos de estudiantes que necesites
}

student_code = None  # Variable global para guardar el código del estudiante

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Buenos Días, soy el bot de la FISI, ¿Ingresa tu código?')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global student_code
    text = message.text  # Obtenemos el texto del mensaje
    if text in student_codes:
        student_code = text  # Guardamos el código del estudiante
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('Lunes')
        itembtn2 = types.KeyboardButton('Martes')
        itembtn3 = types.KeyboardButton('Miércoles')
        itembtn4 = types.KeyboardButton('Jueves')
        itembtn5 = types.KeyboardButton('Viernes')
        itembtn6 = types.KeyboardButton('Sábado')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
        bot.send_message(message.chat.id, f"Hola {student_codes[text]}, ¿Qué día necesitas?", reply_markup=markup)
    elif text in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]:
        courses = student_courses[student_code][text]
        reply = "\n".join([f"{course[0]} en {course[1]}" for course in courses])
        bot.reply_to(message, reply)
    else:
        bot.reply_to(message, f"Lo siento, ese código no está registrado.")
bot.polling()