from .recipe import Recipe


class RecipeBook:
    def __init__(self, name: str, recipes: list[Recipe]|None = None):
        self.name = name
        self.recipes = recipes if recipes is not None else []
    
    def search_by_name(self, query):
        lower_query = query.lower()
        return [recipe for recipe in self.recipes if lower_query in recipe.name.lower()]