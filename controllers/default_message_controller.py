from controllers.base.base_controller import BaseController


class DefaultMessageController(BaseController):
    def __init__(self, bot):
        super().__init__(bot)
        self.default_message = "🍴 Oops! It looks like I didn't understand your message. Please type /help to see a " \
                               "list of available commands and learn how to use the Recipe Bot. If you have any " \
                               "questions or feedback, feel free to contact us. Happy cooking! 🍳"

    def send_default(self, message):
        self.bot.send_message(message.from_user.id, self.default_message)