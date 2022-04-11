from datetime import date
from profile import Profile

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from recipes_app.recipes.models import Recipe
UserModel = get_user_model()


class RecipeModelTest(TestCase):

    VALID_USER_DATA = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }

    VALID_RECIPE_DATA = {
        'recipe_name': 'Recipe',
        'ingredients': 'first, second',
        'recipe_picture': 'recipe.jpg',
        'how_to_make': 'How to make',
        'created_on': '2022-04-10 00:00:00',
        'category': 'Soups',
    }

    def test_recipe_create__when_all_data_is_valid__expect_success(self):
        user = UserModel(**self.VALID_USER_DATA)
        user.save()
        recipe = Recipe(
            recipe_name=self.VALID_RECIPE_DATA['recipe_name'],
            ingredients=self.VALID_RECIPE_DATA['ingredients'],
            recipe_picture=self.VALID_RECIPE_DATA['recipe_picture'],
            how_to_make=self.VALID_RECIPE_DATA['how_to_make'],
            created_on=self.VALID_RECIPE_DATA['created_on'],
            category=self.VALID_RECIPE_DATA['category'],
            created_by_id=user.id
        )
        recipe.save()
        self.assertIsNotNone(recipe.pk)

    def test_recipe_create__when_recipe_picture_is_empty__expected_to_fail(self):
        user = UserModel(**self.VALID_USER_DATA)
        user.save()
        recipe_picture = ''
        recipe = Recipe(
            recipe_name=self.VALID_RECIPE_DATA['recipe_name'],
            ingredients=self.VALID_RECIPE_DATA['ingredients'],
            recipe_picture=recipe_picture,
            how_to_make=self.VALID_RECIPE_DATA['how_to_make'],
            created_on=self.VALID_RECIPE_DATA['created_on'],
            category=self.VALID_RECIPE_DATA['category'],
            created_by_id=user.id
        )
        with self.assertRaises(ValidationError) as context:
            recipe.full_clean()
            recipe.save()

        self.assertIsNotNone(context.exception)

    def test_recipe_create__when_recipe_ingredients_are_not_separate_by_comma_and_space__expected_to_fail(self):
        user = UserModel(**self.VALID_USER_DATA)
        user.save()
        ingredients = ',one  ,two  five   '
        recipe = Recipe(
            recipe_name=self.VALID_RECIPE_DATA['recipe_name'],
            ingredients=ingredients,
            recipe_picture=self.VALID_RECIPE_DATA['recipe_picture'],
            how_to_make=self.VALID_RECIPE_DATA['how_to_make'],
            created_on=self.VALID_RECIPE_DATA['created_on'],
            category=self.VALID_RECIPE_DATA['category'],
            created_by_id=user.id
        )
        with self.assertRaises(ValidationError) as context:
            recipe.full_clean()
            recipe.save()

        self.assertIsNotNone(context.exception)
