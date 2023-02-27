import os

from controllers.default_message_controller import DefaultMessageController
from controllers.recipe_search_controller import RecipeSearchController
from controllers.random_recipe_controller import RandomRecipeController
from controllers.start_controller import StartController
from controllers.help_controller import HelpController
from factories.bot_factory import BotFactory

bot_factory = BotFactory()
bot = bot_factory.create_bot()

recipe_api_base_url = os.getenv("RECIPE_API_BASE_URL")

recipe_searcher = RecipeSearchController(bot, recipe_api_base_url)
random_recipe_controller = RandomRecipeController(bot, recipe_api_base_url)
start_controller = StartController(bot)
help_controller = HelpController(bot)
default_message_controller = DefaultMessageController(bot)

bot.message_handler(commands=["search"])(recipe_searcher.send_search)
bot.message_handler(commands=["random"])(random_recipe_controller.send_random)
bot.message_handler(commands=["start"])(start_controller.send_welcome)
bot.message_handler(commands=["help"])(help_controller.send_help)
bot.message_handler(content_types=["text"])(default_message_controller.send_default)


bot.polling(none_stop=True, interval=0)
