import os

import telebot
from dotenv import load_dotenv

from application.product.add_product import AddProduct

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Use Cases
add_product = AddProduct(bot)


@bot.message_handler(commands=["add_product"])
def add_product_handler(message):
    add_product.start_application(message)


print("Bot running.")
bot.infinity_polling()
