import unittest
import sys
sys.path.append("..")
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
