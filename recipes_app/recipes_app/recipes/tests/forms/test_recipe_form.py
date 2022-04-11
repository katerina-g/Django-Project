from django.test import TestCase

from recipes_app.recipes.forms import CreateRecipeForm


class RecipeFormTests(TestCase):

    def test_recipe_form_save__when_data_is_invalid__expect_to_fail(self):
        data = {
            'recipe_name': 'Test',
            'ingredients': 'test1 test2  test3',
            'recipe_picture': 'http://test.picture/url.png',
            'how_to_make': 'Test test test',
            'category': 'Soups',

        }
        form = CreateRecipeForm(data)
        self.assertFalse(form.is_valid())
