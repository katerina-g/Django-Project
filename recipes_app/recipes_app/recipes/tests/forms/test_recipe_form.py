from django.test import TestCase

from recipes_app.recipes.forms import CreateRecipeForm


class RecipeFormTests(TestCase):
    def test_recipe_form_save__when_data_is_valid__expected_success(self):
        data = {
            'recipe_name': 'Test',
            'ingredients': 'test, test',
            'recipe_picture': '',
            'how_to_make': 'Testtesttest',
            'category': 'Soups',
        }

        form = CreateRecipeForm(data)
        print(data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_recipe_form_save__when_data_is_invalid__expect_to_fail(self):
        data = {
            'recipe_name': 'Test',
            'ingredients': 'test1 test2  test3',
            'recipe_picture': 'http://test.picture/url.png',
            'how_to_make': 'Test test test',

        }
        form = CreateRecipeForm(data)
        self.assertFalse(form.is_valid())