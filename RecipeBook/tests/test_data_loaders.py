import unittest
import unittest.mock
import os
from src.constants import DietaryTag, MeasurementUnits
from src.data_loaders import CSVDataLoader
from src.ingredients import Ingredient, RecipeIngredient
from src.recipe import Instruction,Recipe

class TestCSVDataLoader(unittest.TestCase):

    def test_load_data(self):
        semolina = Ingredient("Semolina", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN, DietaryTag.NUT_FREE])
        water = Ingredient("Water", [DietaryTag.NOT_APPLICABLE])
        mock_ingredient_repo = unittest.mock.Mock()
        mock_ingredient_repo.get_ingredient.side_effect = [semolina, water]
        data_file = os.path.realpath(os.path.dirname(__file__)) + "/recipes_test_data.csv"
        parsed_data = CSVDataLoader(mock_ingredient_repo).load_data(data_file)
        recipe_semolina = RecipeIngredient(semolina, 100, MeasurementUnits.GM)
        recipe_water = RecipeIngredient(water, 200, MeasurementUnits.ML)
        instructions = [
            Instruction(1,"Mix the ingredients and kneed a dough", 3, "Bowl"),
            Instruction(2,"Roll and cut", 10, "Rolling pin;Board"),
            Instruction(3,"Dry it", 120, "Bar"),
        ]
        expected_recipe = Recipe("Pasta", [recipe_semolina, recipe_water], instructions)
        self.assertEqual(expected_recipe, parsed_data[0])
