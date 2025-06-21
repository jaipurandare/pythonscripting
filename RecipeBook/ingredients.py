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
        self.dietary_tags = self.ingredient.dietary_tags

    def __repr__(self):
        return f"{self.ingredient.name} : {self.quantity} {self.unit}"