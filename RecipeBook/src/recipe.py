from .ingredients import RecipeIngredient


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
        return f"name: {self.name}, ingredients: {self.ingredients}, \n instructions: {self.instructions} "