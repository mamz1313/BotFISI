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
# Agrega aquí todos los códigos y cursos de estudiantes que necesites
# Diccionario que mapea los códigos de los estudiantes a sus cursos y salones
student_courses = {
     "19200171": {
        "Lunes": [("INTELIGENCIA ARTIFICIAL 3.0", "Salón 101", "8:00 AM", "10:00 AM"), ("INVESTIGACIÓN OPERATIVA", "Salón 102", "10:30 AM", "12:30 PM")],
        "Martes": [("LENGUAJES Y COMPILADORES", "Salón 201", "9:00 AM", "11:00 AM")],
        "Miércoles": [("INTERNET DE LAS COSAS 3.0", "Salón 202", "8:00 AM", "10:00 AM"), ("SISTEMAS OPERATIVOS", "Salón 203", "10:30 AM", "12:30 PM")],
        "Jueves": [("REDES, TRANSMISIÓN Y AUTOMATIZACIÓN Y CONTROL", "Salón 204", "9:00 AM", "11:00 AM")],
        "Viernes": [("PROGRAMACIÓN PARALELA 3.0", "Salón 205", "8:00 AM", "10:00 AM"), ("METODOLOGIA DE LA ELABORACIÓN DE TESIS", "Salón 206", "10:30 AM", "12:30 PM")],
        "Sábado": [("SISTEMAS DISTRIBUIDOS 3.0", "Salón 207", "9:00 AM", "11:00 AM")]
    },
    "20200218": {
        "Lunes": [("INTELIGENCIA ARTIFICIAL 3.0", "Salón 101", "8:00 AM", "10:00 AM"), ("INVESTIGACIÓN OPERATIVA", "Salón 102", "10:30 AM", "12:30 PM")],
        "Martes": [("LENGUAJES Y COMPILADORES", "Salón 201", "9:00 AM", "11:00 AM")],
        "Miércoles": [("INTERNET DE LAS COSAS 3.0", "Salón 202", "8:00 AM", "10:00 AM"), ("SISTEMAS OPERATIVOS", "Salón 203", "10:30 AM", "12:30 PM")],
        "Jueves": [("REDES, TRANSMISIÓN Y AUTOMATIZACIÓN Y CONTROL", "Salón 204", "9:00 AM", "11:00 AM")],
        "Viernes": [("PROGRAMACIÓN PARALELA 3.0", "Salón 205", "8:00 AM", "10:00 AM"), ("METODOLOGIA DE LA ELABORACIÓN DE TESIS", "Salón 206", "10:30 AM", "12:30 PM")],
        "Sábado": [("SISTEMAS DISTRIBUIDOS 3.0", "Salón 207", "9:00 AM", "11:00 AM")]
    },
    "19200186": { 
        "Lunes": [("INTELIGENCIA ARTIFICIAL 3.0", "Salón 101", "8:00 AM", "10:00 AM"), ("INVESTIGACIÓN OPERATIVA", "Salón 102", "10:30 AM", "12:30 PM")],
        "Martes": [("LENGUAJES Y COMPILADORES", "Salón 201", "9:00 AM", "11:00 AM")],
        "Miércoles": [("INTERNET DE LAS COSAS 3.0", "Salón 202", "8:00 AM", "10:00 AM"), ("SISTEMAS OPERATIVOS", "Salón 203", "10:30 AM", "12:30 PM")],
        "Jueves": [("REDES, TRANSMISIÓN Y AUTOMATIZACIÓN Y CONTROL", "Salón 204", "9:00 AM", "11:00 AM")],
        "Viernes": [("PROGRAMACIÓN PARALELA 3.0", "Salón 205", "8:00 AM", "10:00 AM"), ("METODOLOGIA DE LA ELABORACIÓN DE TESIS", "Salón 206", "10:30 AM", "12:30 PM")],
        "Sábado": [("SISTEMAS DISTRIBUIDOS 3.0", "Salón 207", "9:00 AM", "11:00 AM")]
    },
    # Agrega aquí todos los códigos y cursos de estudiantes que necesites
    # Agrega aquí todos los códigos y cursos de estudiantes que necesites
}

student_code = None  # Variable global para guardar el código del estudiante

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Buenos Días, soy el bot de la FISI, ¿Ingresa tu código de alumno?')

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
        reply = "\n".join([f"{course[0]} en {course[1]} de {course[2]} a {course[3]}" for course in courses])
        bot.reply_to(message, reply)
    else:
        bot.reply_to(message, f"Lo siento, ese código no está registrado.")
bot.polling()