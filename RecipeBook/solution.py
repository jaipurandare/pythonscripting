from dataclasses import dataclass
from enum import Enum
from constants import DietaryTag
from ingredients import Ingredient, RecipeIngredient

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