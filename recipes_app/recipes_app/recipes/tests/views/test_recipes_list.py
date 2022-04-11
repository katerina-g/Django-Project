from django.test import TestCase
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model

from recipes_app.recipes.models import Recipe

UserModel = get_user_model()


class RecipesListViewTests(TestCase):

    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create(**credentials)

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('all recipes'))

        self.assertTemplateUsed(response, 'recipes/all_recipes.html')

    def test_get__when_two_recipes__expect_context_to_contain_two_recipes(self):
        user = self.__create_user()

        recipes_to_create = (
            Recipe(recipe_name='recipe', ingredients='one, two', recipe_picture='recipe.jpg', how_to_make='blabla',
                   created_by=user, category=Recipe.SOUPS),
            Recipe(recipe_name='recipe2', ingredients='one, two', recipe_picture='recipe.jpg', how_to_make='blabla',
                   created_by=user, category=Recipe.SOUPS),
        )
        Recipe.objects.bulk_create(recipes_to_create)
        response = self.client.get(reverse_lazy('all recipes'))

        recipes = response.context['object_list']
        self.assertEqual(len(recipes), 2)
