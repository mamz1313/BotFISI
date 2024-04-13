import telebot

bot = telebot.TeleBot("6441365825:AAHWDtuHdobmZ0CR7Iu40BRi-SleD0_fpYg")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Karen no esta renegando, esta programando')

bot.polling()