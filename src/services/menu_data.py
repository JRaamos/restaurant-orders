import csv
from typing import Dict

from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._process_data(source_path)

    def _process_data(self, source_path: str) -> None:
        dish_table: Dict[str, Dish] = {}

        with open(source_path) as csv_file:
            data = csv.DictReader(csv_file)

            for row in data:
                dish_name, price, ingredient_name, recipe_amount = (
                    row["dish"],
                    float(row["price"]),
                    row["ingredient"],
                    int(row["recipe_amount"]),
                )

                dish = dish_table.setdefault(dish_name, Dish(dish_name, price))
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)

                self.dishes.add(dish)
