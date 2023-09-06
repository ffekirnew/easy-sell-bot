from telebot import TeleBot

from core import config
from handlers.register_handlers import RegisterHandlers

# Create bot instance
bot = TeleBot(config.BOT_TOKEN, num_threads=5)

# Register Handlers
RegisterHandlers(bot).register_handlers()

if __name__ == "__main__":
    print("Bot running.")
    bot.infinity_polling()
