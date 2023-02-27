from telebot import TeleBot


class BaseController:
    def __init__(self, bot: TeleBot):
        self.bot = bot
