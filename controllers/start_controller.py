import logging

from controllers.base.base_controller import BaseController


class StartController(BaseController):
    def __init__(self, bot):
        super().__init__(bot)
        self.intro_message = "🔍 Looking for some inspiration in the kitchen? We've got you covered! Simply search " \
                             "for recipes by ingredients, cuisine, dietary restrictions, and more. \n\n📝 Create a " \
                             "shopping list based on your chosen recipes and never forget an ingredient again. " \
                             "\n\n🗓️ Plan your meals for the week ahead and save time on grocery shopping and meal " \
                             "prep. \n\n🌟 Love a recipe? Share it with friends and family and rate and review " \
                             "recipes to help others find their new favorite dish. \n\n👤 Create a user profile with " \
                             "your dietary preferences and cooking skills to get personalized recipe suggestions. " \
                             "\n\n👋 Let's get cooking!"

    def send_welcome(self, message):
        logging.info("Sending welcome message...")
        chat_id = message.chat.id
        self.bot.send_message(chat_id, self.intro_message)