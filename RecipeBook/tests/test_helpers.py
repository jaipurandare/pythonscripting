import io
import unittest
import unittest.mock
import sys
sys.path.append("..")
from src.helpers import log_recipe_action
from src.recipe import Recipe

class DummyClass:
    name = "Dummy class"
    @log_recipe_action("test_action")
    def test_action(self, *args, **kwargs):
        pass

class TestHelpers(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_log_recipe_action(self, mock_stdout):
        dummy_recipe = Recipe("dummy",None,None)
        DummyClass().test_action(dummy_recipe)
        expected_log = "TEST_ACTION Recipe dummy in Dummy class book\n"
        self.assertEqual(expected_log, mock_stdout.getvalue())