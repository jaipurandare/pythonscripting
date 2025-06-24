import unittest
import unittest.mock
import sys
sys.path.append("..")

def mocked_decorator(func):
    def wrapper(self, *args, **kwargs):
        return func(self, *args, **kwargs)
    return wrapper
import src.helpers
src.helpers.log_recipe_action = unittest.mock.Mock(return_value=mocked_decorator)
# This mocking has to be done before recipeBook module is imported.
# since log_recipe_action is used as decorator it gets called immediately.

from src.constants import DietaryTag, MeasurementUnits
from src.ingredients import Ingredient, RecipeIngredient
from src.recipe import Recipe
from src.recipeBook import RecipeBook

class TestRecipeBook(unittest.TestCase):

    def test_initialize_recipe_book(self):
        # This function should initialize a recipe book
        # For the sake of this example, we will just check if it exists
        my_book = RecipeBook("MyBook")
        self.assertIsNotNone(my_book)
        self.assertEqual(my_book.name, "MyBook")
    
    def test_search_by_name_returns_all_containing_query(self):
        pasta = Recipe("pasta", [], [])
        omlet = Recipe("omlet", [], [])
        macaroni_pasta = Recipe("macaroni pasta", [], [])
        book = RecipeBook("book", [pasta, omlet, macaroni_pasta])
        actual_search_result = sorted(book.search_by_name("Pasta"), key=lambda recipe: recipe.name)
        expected_result = [macaroni_pasta, pasta]
        self.assertListEqual(expected_result, actual_search_result)

    def test_search_by_ingredient_returns_all_containing_query(self):
        egg = Ingredient("egg", [DietaryTag.GLUTEN_FREE, DietaryTag.NON_VEGETARIAN, DietaryTag.NUT_FREE])
        salt = Ingredient("salt", [DietaryTag.GLUTEN_FREE, DietaryTag.NUT_FREE, DietaryTag.VEGAN, DietaryTag.VEGETARIAN])
        tsp_salt = RecipeIngredient(salt,1, MeasurementUnits.TEA_SPOON)
        pasta = Recipe("pasta", [RecipeIngredient(egg,1, MeasurementUnits.COUNT), tsp_salt], [])
        omlet = Recipe("omlet", [RecipeIngredient(egg,2, MeasurementUnits.COUNT), tsp_salt], [])
        macaroni_pasta = Recipe("macaroni pasta", [tsp_salt], [])
        book = RecipeBook("book", [pasta, omlet, macaroni_pasta])
        actual_search_result = sorted(book.search_by_ingredient("Egg"), key=lambda recipe: recipe.name)
        expected_result = [omlet, pasta]
        self.assertListEqual(expected_result, actual_search_result)

    def test_add_recipe(self):
        macaroni_pasta = Recipe("macaroni pasta", [], [])
        my_book = RecipeBook("my_book")
        my_book.add_recipe(macaroni_pasta)
        expected_recipes = [macaroni_pasta]
        self.assertListEqual(expected_recipes, my_book.recipes)
        src.helpers.log_recipe_action.assert_called_once()

    def test_add_recipe_raise_exception_if_not_recipe(self):
        my_book = RecipeBook("my_book")
        exception_message = "Expected type Recipe but passed <class 'NoneType'>"
        with self.assertRaises(TypeError) as ex:
            my_book.add_recipe(None)
        self.assertEqual(exception_message,str(ex.exception))
        src.helpers.log_recipe_action.assert_called_once()
