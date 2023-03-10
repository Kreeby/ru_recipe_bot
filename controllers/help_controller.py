import logging

from controllers.base.base_controller import BaseController


class HelpController(BaseController):
    def __init__(self, bot):
        super().__init__(bot)
        self.help_message = "š“ Welcome to Recipe Bot! š To use Recipe Bot, search for recipes š² based on " \
                            "ingredients š„¦, cuisine š, and dietary restrictions š„. You can also create a shopping " \
                            "list š, plan meals for the week šļø, and share recipes with friends š„.  Here are some " \
                            "commands to get started: \n\nš /search - Search for recipes \n\nšļø /shoppinglist - " \
                            "View or edit your shopping list \n\nš½ļø /mealplan - Get meal plan suggestions \n\nš¤ " \
                            "/profile - Create or edit your user profile \n\nš© /share - Share a recipe with friends " \
                            "\n\nType /help followed by the command name for more information on how to use each " \
                            "command. Let's get cooking! š³"

    def send_help(self, message):
        logging.info("Sending help message...")
        chat_id = message.chat.id
        self.bot.send_message(chat_id, self.help_message)
