from cProfile import Profile

from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from recipes_app.recipes.models import Recipe

UserModel = get_user_model()


class RecipeDeleteView(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'Test',
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create(**credentials)

    def test_delete_recipe__expect_to_redirect(self):
        user = self.__create_user()
        self.client.force_login(user)
        recipe = Recipe.objects.create(recipe_name='recipe', ingredients='one, two', recipe_picture='recipe.jpg',
                                       how_to_make='blabla',
                                       created_by=user, category=Recipe.SOUPS)
        response = self.client.delete(reverse('delete recipe', kwargs={
            'pk': recipe.id,
        }))

        self.assertEqual(302, response.status_code)

