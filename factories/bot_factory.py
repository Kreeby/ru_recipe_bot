import os
import telebot


class BotFactory:
    def create_bot(self):
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        return telebot.TeleBot(token)
