from abc import ABC, abstractmethod
import csv
from .constants import DietaryTag, MeasurementUnits
from .ingredients import Ingredient, RecipeIngredient, IngredientRepository
from .recipe import Recipe, Instruction

class DataLoader(ABC):

    def __init__(self, ingredient_repo):
        self._ingredient_repo = ingredient_repo
    
    @abstractmethod
    def load_data(self, source):
        pass


class CSVDataLoader(DataLoader):

    def _parse_ingredients(self, column):
        ingredients = []
        for rec_ingre in column.split(":"):
            rec_ingre_data = rec_ingre.split(" ")
            ingredient = self._ingredient_repo.get_ingredient(rec_ingre_data[0])
            quantity = int(rec_ingre_data[1])
            unit = MeasurementUnits.from_str(rec_ingre_data[2])
            ingredients.append(RecipeIngredient(ingredient, quantity, unit))
        return ingredients
    
    def _parse_instructions(self, columns):
        instruction_attribute_separator = ":"
        instructions = []
        for column in columns:
            instruction_data = column.split(instruction_attribute_separator)
            instructions.append( Instruction(int(instruction_data[0]),instruction_data[1], 
                                   int(instruction_data[2]), instruction_data[3])
            )
        return instructions

    def load_data(self, source):
        recipes = []
        with open(source) as df:
            data_reader = csv.reader(df, delimiter=',')
            for row in data_reader:
                name = row[0]
                ingredients = self._parse_ingredients(row[1])
                instrctions = self._parse_instructions(row[2:])
                recipes.append(Recipe(name, ingredients, instrctions))
        return recipes