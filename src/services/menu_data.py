from models.ingredient import Ingredient
from models.dish import Dish

import csv


class MenuData:
    def __init__(self, source_path: str):
        self._path = source_path
        self.dishes = set()
        self.read_menu_data()

    def read_menu_data(self):
        with open(self._path, encoding="utf-8") as file:
            menu = csv.reader(file)
            next(menu)

            for row in menu:
                dish_name, price, ingredient_name, recipe_amount = row

                dish = next(
                    (d for d in self.dishes if d.name == dish_name), None
                )
                if dish is None:
                    price = float(price)
                    dish = Dish(dish_name, price)
                    self.dishes.add(dish)

                recipe_amount = int(recipe_amount)
                ingredient = next(
                    (
                        i
                        for i in dish.recipe.keys()
                        if i.name == ingredient_name
                    ),
                    None,
                )
                if ingredient is None:
                    ingredient = Ingredient(ingredient_name)
                    dish.add_ingredient_dependency(ingredient, recipe_amount)
                else:
                    dish.recipe[ingredient] += recipe_amount
