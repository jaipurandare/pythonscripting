from .ingredients import RecipeIngredient


class Instruction:
    def __init__(self, step_number: int, description: str, prep_time: int, equipment: str):
        self.step_number = step_number
        self.description = description
        self.prep_time = prep_time
        self.equipment = equipment
    
    def __repr__(self):
        return f"{self.step_number}: {self.description} \nprep_time: {self.prep_time}\nequipment: {self.equipment}"
    
    def __eq__(self, value):
        return self.step_number == value.step_number and \
        self.description == value.description and \
        self.prep_time == value.prep_time and \
        self.equipment == value.equipment

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
    
    def __eq__(self, value):
        return type(self) == type(value) and \
        self.name == value.name and \
        sorted(self.ingredients, key=lambda i: i.name) == sorted(value.ingredients, key=lambda i: i.name)  and \
        sorted(self.instructions, key=lambda i: i.step_number) == sorted(value.instructions, key=lambda i: i.step_number)