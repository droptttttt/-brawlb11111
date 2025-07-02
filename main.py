import telebot
from telebot import types

BOT_TOKEN = "8025356562:AAEUwxM1OQjHtUsrlbbXTpQol2UPx8bpnD4"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Нажми меня")
    bot.send_message(message.chat.id, "Привет! Нажми кнопку 👇", reply_markup=markup)

@bot.message_handler(func=lambda msg: msg.text == "Нажми меня")
def clicked(message):
    bot.send_message(message.chat.id, "Ты нажал кнопку!")

bot.infinity_polling()
