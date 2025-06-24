import unittest
from src.recipe import Recipe, Instruction
from src.ingredients import Ingredient, RecipeIngredient
from src.constants import DietaryTag, MeasurementUnits


class TestRecipe(unittest.TestCase):

    cooking_instructions = [Instruction(1,"Cook it", 10, "pan")]
    
    def test_initialize_recipe(self):
        # This function should initialize a recipe
        tomato = Ingredient("Tomato", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN])
        pasta = Ingredient("Pasta", [DietaryTag.VEGAN, DietaryTag.VEGETARIAN])
        two_tomatoes = RecipeIngredient(tomato, 2, MeasurementUnits.COUNT)
        pasta_4oz = RecipeIngredient(pasta, 4, MeasurementUnits.OZ)
        pasta_name = "Pasta with Tomato"
        my_recipe = Recipe(pasta_name, [two_tomatoes, pasta_4oz],self.cooking_instructions)
        self.assertIsNotNone(my_recipe)
        self.assertEqual(my_recipe.name, pasta_name)
        self.assertListEqual(my_recipe.ingredients, [two_tomatoes, pasta_4oz])

    def test_get_dietary_tags(self):
        tomato = Ingredient("Tomato", {DietaryTag.VEGAN, DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE, DietaryTag.NUT_FREE})
        egg = Ingredient("Egg", {DietaryTag.NON_VEGETARIAN, DietaryTag.GLUTEN_FREE, DietaryTag.NUT_FREE})
        salt = Ingredient("Salt", {DietaryTag.VEGAN, DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE, DietaryTag.NUT_FREE})
        pinenut = Ingredient("PineNut", {DietaryTag.VEGAN, DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE})
        one_tomato = RecipeIngredient(tomato, 1, MeasurementUnits.COUNT)
        three_eggs = RecipeIngredient(egg, 3, MeasurementUnits.COUNT)
        topping_pinenut = RecipeIngredient(pinenut, 1, MeasurementUnits.TEA_SPOON)
        salt_to_taste = RecipeIngredient(salt, 0, MeasurementUnits.TO_TASTE)
        omlet = Recipe("Omlet", [three_eggs, one_tomato, topping_pinenut, salt_to_taste], self.cooking_instructions)
        expected_dietary_tags = sorted({DietaryTag.VEGAN, DietaryTag.VEGETARIAN, DietaryTag.GLUTEN_FREE, DietaryTag.NUT_FREE, DietaryTag.NON_VEGETARIAN })
        self.assertListEqual(expected_dietary_tags, sorted(omlet.get_dietary_tags()))
    
    def test_empty_dietary_tags_for_no_recipe_ingredients(self):
        zero_ingredients_recipe = Recipe("Zero Ingredients", [], [])
        self.assertEqual(set(), zero_ingredients_recipe.get_dietary_tags())
