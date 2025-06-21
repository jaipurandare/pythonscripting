from dataclasses import dataclass
from enum import Enum
from constants import DietaryTag
from ingredients import Ingredient, RecipeIngredient


class Instruction:
    def __init__(self, step_number: int, description: str, prep_time: int, equipment: str):
        self.step_number = step_number
        self.description = description
        self.prep_time = prep_time
        self.equipment = equipment
    
    def __repr__(self):
        return f"{self.step_number} {self.description}"

class Recipe:
    def __init__(self, name: str, ingredients: list[RecipeIngredient], instructions: list[Instruction]):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def get_dietary_tags(self):
        tags = set()
        if self.ingredients:
            tags = set.union(*[ingredient.dietary_tags for ingredient in self.ingredients])
        return tags
    
    def __repr__(self):
        return f"name: {self.name}, ingredients: {",".join(self.ingredients)}, \n instructions: {self.instructions} "


class RecipeBook:
    def __init__(self, name: str, recipes: list[Recipe]|None = None):
        self.name = name
        self.recipes = recipes if recipes is not None else []
    
    def search_by_name(self, query):
        lower_query = query.lower()
        return [recipe for recipe in self.recipes if lower_query in recipe.name.lower()]

# Finally, we discussed the issue of creating a repository of ingredients
# We don't really want to list them all like this:
flour = Ingredient("Flour", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN])
egg = Ingredient("Egg", [DietaryTag.NUT_FREE])

# Here are some options
# Option 1
ingredient_repository_dict = {
    "Flour": Ingredient("Flour", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN]),
    "Egg": Ingredient("Egg", [DietaryTag.NUT_FREE]),
}

# Option 2
@dataclass
class IngredientRepository:
    flour: Ingredient
    egg: Ingredient

ingredient_repository = IngredientRepository(
    Ingredient("Flour", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN]),
    Ingredient("Egg", [DietaryTag.NUT_FREE]),
)

# Option 3
class IngredientRepository(Enum):
    FLOUR = Ingredient("Flour", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN])
    EGG = Ingredient("Egg", [DietaryTag.NUT_FREE])

# Option 4
class IngredientRepository:
    def __init__(self, name):
        self.name = name
        self._ingredients = {}

    def add_ingredient(self, ingredient: Ingredient):
        if ingredient.name.upper() in self._ingredients:
            raise ValueError("Ingredient already exists")
        self._ingredients[ingredient.name.upper()] = ingredient

    def __getattr__(self, name):
        name = name.upper()
        if name in self._ingredients:
            return self._ingredients[name]
        raise AttributeError("Ingredient not found")


repository = IngredientRepository("repository")
repository.add_ingredient(Ingredient("Flour", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN]))
print(repository.FLOUR)

flour_in_cake = RecipeIngredient(flour, 100, "g")
egg_in_cake = RecipeIngredient(egg, 4, "units")

# cake = Recipe("Cake", [flour_in_cake, egg_in_cake])

# tomato_pasta = Recipe("", [tomato, pasta])
# salad = Recipe("", [tomato])