import logging

import requests
from telebot import types

from controllers.base.base_controller import BaseController
from models.recipe import Recipe


def get_keyboard(specific_recipe_list):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    for i in specific_recipe_list:
        button = types.KeyboardButton(i["strMeal"])
        keyboard.add(button)
    return keyboard


def get_recipe_by_name(text, specific_recipe_list):
    for recipe in specific_recipe_list:
        if recipe["strMeal"] == text:
            return Recipe(**recipe)


class RecipeSearchController(BaseController):

    def __init__(self, bot, recipe_api_base_url):
        super().__init__(bot)
        self.search_message = "👋 Hi there! What would you like to search for? You can search by ingredients 🍅, " \
                              "cuisine 🍝, dietary restrictions 🥗, meal type 🍲, cooking time ⏰, and difficulty " \
                              "level 🌟. \n\n To search by ingredients, type /search ingredients 🍅. To search by " \
                              "cuisine, type /search cuisine 🍝. To search by dietary restrictions, type /search diet " \
                              "🥗. To search by meal type, type /search meal 🍲. To search by cooking time, " \
                              "type /search time ⏰. To search by difficulty level, type /search difficulty 🌟. " \
                              "\n\nYou can also get a random recipe by typing /random 🎲. To cancel the search, " \
                              "type /cancel ❌. Let's find some delicious recipes! 🍽️"
        self.not_found_meal_message = "🍴 Sorry, we couldn't find any recipes with that name. Please try another " \
                                      "search term or refine your search criteria. If you need help, type /help for " \
                                      "more information on how to use the Recipe Bot. Happy cooking! 🍳"
        self.recipe_api_base_url = recipe_api_base_url

    def send_search(self, message):
        logging.info("Sending search message...")
        chat_id = message.chat.id
        search_text = message.text[8:]
        if len(search_text) == 0:
            self.bot.send_message(chat_id, self.search_message)
        elif search_text.startswith("meal"):
            search_word = search_text[5:]
            specific_recipe_list = self.get_specific_recipe(search_word)
            if not specific_recipe_list:
                self.bot.send_message(chat_id, self.not_found_meal_message)
            elif len(specific_recipe_list) > 1:
                self.bot.send_message(chat_id, "Please choose an option 🍅:",
                                      reply_markup=get_keyboard(specific_recipe_list))
                self.bot.register_next_step_handler(message, self.send_chosen_recipe, specific_recipe_list)
            else:
                recipe = Recipe(**specific_recipe_list[0])
                recipe_message = "🍴 Here's a delicious recipe just for you! 🎲 \n\n🍲 Category: {} \n\n🍽️ Name: " \
                                 "{} \n\n🌎 Area: {} \n\n📝 Instructions: {}\n\n 📷 Image: {} \n\n🎥 Youtube Video " \
                                 "URL: {} \n\nEnjoy your meal! 🍅".format(recipe.strCategory,
                                                                         recipe.strMeal,
                                                                         recipe.strArea,
                                                                         recipe.strInstructions,
                                                                         recipe.strMealThumb,
                                                                         recipe.strYoutube)
                self.bot.send_message(chat_id, recipe_message)

    def get_specific_recipe(self, msg):
        endpoint = self.recipe_api_base_url + "search.php"
        query_parameters = {'s': msg}
        json_response = requests.get(endpoint, params=query_parameters).json()
        response_list = json_response["meals"]
        return response_list

    def send_chosen_recipe(self, message, specific_recipe_list):
        chat_id = message.chat.id
        recipe = get_recipe_by_name(message.text, specific_recipe_list)
        recipe_message = "🍴 Here's a delicious recipe just for you! 🎲 \n\n🍲 Category: {} \n\n🍽️ Name: {} " \
                         "\n\n🌎 Area: {} \n\n📝 Instructions: {}\n\n 📷 Image: {} \n\n🎥 Youtube Video URL: {} " \
                         "\n\nEnjoy your meal! 🍅".format(recipe.strCategory,
                                                         recipe.strMeal,
                                                         recipe.strArea,
                                                         recipe.strInstructions,
                                                         recipe.strMealThumb,
                                                         recipe.strYoutube)
        self.bot.send_message(chat_id, recipe_message, reply_markup=types.ReplyKeyboardRemove())
