from dataclasses import dataclass
from .constants import DietaryTag


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
        self.name = self.ingredient.name

    def __repr__(self):
        return f"{self.ingredient.name} : {self.quantity} {self.unit}"
    
    def __eq__(self, value):
        return type(self) == type(value) and \
            self.name == value.name and \
            self.quantity == value.quantity and \
            self.unit == value.unit


class IngredientRepository:
    
    def get_ingredient(self, name):
        pass