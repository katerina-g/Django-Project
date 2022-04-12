import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from recipes_app.recipes.forms import CreateRecipeForm
from django.conf import settings


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

    def test_recipe_form_save__when_data_is_valid__expect_to_be_true(self):
        file_path = os.path.join(settings.BASE_DIR, 'recipes_app/recipes/tests/cat.jpg')
        data = {
            'recipe_name': 'Test',
            'ingredients': 'test1, test2, test3',
            'how_to_make': 'Test test test',
            'category': 'Soups',
        }

        with open(file_path, 'rb') as f:
            form = CreateRecipeForm(data=data, files={'recipe_picture': SimpleUploadedFile('cat.jpg', f.read())})
            self.assertTrue(form.is_valid())