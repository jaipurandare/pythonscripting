from .helpers import log_recipe_action
from .recipe import Recipe


class RecipeBook:
    def __init__(self, name: str, recipes: list[Recipe]|None = None):
        self.name = name
        self.recipes = recipes if recipes is not None else []
    
    def search_by_name(self, query):
        lower_query = query.lower()
        return [recipe for recipe in self.recipes if lower_query in recipe.name.lower()]
    
    def search_by_ingredient(self, query):
        lower_query = query.lower()
        return [recipe for recipe in self.recipes if any(lower_query in ingredient.name.lower() for ingredient in recipe.ingredients)]
    
    @log_recipe_action("add")
    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes.append(recipe)
        else:
            raise TypeError(f"Expected type Recipe but passed {type(recipe)}")