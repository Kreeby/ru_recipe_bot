import logging

import requests

from controllers.base.base_controller import BaseController
from models.recipe import Recipe


class RandomRecipeController(BaseController):
    def __init__(self, bot, recipe_api_base_url):
        super().__init__(bot)
        self.recipe_api_base_url = recipe_api_base_url

    def send_random(self, message):
        logging.info("Sending random recipe message...")
        random_recipe = self.get_random_recipe()
        random_recipe_message = "🍴 Here's a delicious recipe just for you! 🎲 \n\n🍲 Category: {} \n\n🍽️ Name: {} " \
                                "\n\n🌎 Area: {} \n\n📝 Instructions: {}\n\n 📷 Image: {} \n\n🎥 Youtube Video URL: {} " \
                                "\n\nEnjoy your meal! 🍅".format(random_recipe.strCategory,
                                                                random_recipe.strMeal,
                                                                random_recipe.strArea,
                                                                random_recipe.strInstructions,
                                                                random_recipe.strMealThumb,
                                                                random_recipe.strYoutube)
        chat_id = message.chat.id
        self.bot.send_message(chat_id, random_recipe_message)

    def get_random_recipe(self):
        endpoint = self.recipe_api_base_url + "random.php"
        json_response = requests.get(endpoint).json()

        random_recipe = Recipe(**json_response["meals"][0])
        return random_recipe
