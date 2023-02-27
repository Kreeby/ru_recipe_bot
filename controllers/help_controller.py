import logging

from controllers.base.base_controller import BaseController


class HelpController(BaseController):
    def __init__(self, bot):
        super().__init__(bot)
        self.help_message = "🍴 Welcome to Recipe Bot! 🔍 To use Recipe Bot, search for recipes 🍲 based on " \
                            "ingredients 🥦, cuisine 🍝, and dietary restrictions 🥑. You can also create a shopping " \
                            "list 🛒, plan meals for the week 🗓️, and share recipes with friends 👥.  Here are some " \
                            "commands to get started: \n\n🔍 /search - Search for recipes \n\n🛍️ /shoppinglist - " \
                            "View or edit your shopping list \n\n🍽️ /mealplan - Get meal plan suggestions \n\n👤 " \
                            "/profile - Create or edit your user profile \n\n📩 /share - Share a recipe with friends " \
                            "\n\nType /help followed by the command name for more information on how to use each " \
                            "command. Let's get cooking! 🍳"

    def send_help(self, message):
        logging.info("Sending help message...")
        chat_id = message.chat.id
        self.bot.send_message(chat_id, self.help_message)
