from dataclasses import dataclass
from constants import DietaryTag


@dataclass
class Ingredient:
    name: str
    dietary_tags: set[DietaryTag]

class RecipeIngredient:
    def __init__(self, ingredient: Ingredient, quantity: int | float, unit: str):
        self.ingredient = ingredient
        self.quantity = quantity
        self.unit = unit

    @property
    def dietary_tags(self):
        return self.ingredient.dietary_tags
