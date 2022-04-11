from datetime import date

from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse

from recipes_app.main.models import Like
from recipes_app.recipes.models import Recipe

UserModel = get_user_model()


class RecipeDetailsViewTests(TestCase):
    VALID_RECIPE_DATA = {
        'recipe_name': 'Recipe',
        'ingredients': 'first, second',
        'recipe_picture': 'recipe.jpg',
        'how_to_make': 'How to make',
        'created_on': date.today(),
        'category': Recipe.SOUPS,
    }

    logged_in_user_email = 'test@abv.bg'
    logged_in_user_password = '123456trewq'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )

    def __create_recipe(self, **kwargs):
        return Recipe.objects.create(**kwargs)

    def __create_recipe_for_profile_user(self, user):
        recipe = Recipe.objects.create(
            **self.VALID_RECIPE_DATA,
            created_by_id=user.id
        )
        return recipe

    def __create_recipe_with_like(self, like_user, **kwargs):
        recipe = self.__create_recipe(**kwargs)
        Like.objects.create(
            recipe=recipe,
            user=like_user,
        )
        return recipe

    def test_get_recipe_details__when_recipe_exists_and_is_creator__should_return_details_for_his_creator(self):
        self.client.force_login(self.user)
        recipe = self.__create_recipe_for_profile_user(self.user)

        response = self.client.get(reverse('recipe details', kwargs={
            'pk': recipe.id,
        }))
        self.assertTrue(response.context['is_creator'])

    def test_get_recipe_details__when_user_is_not_creator__should_return_detail_for_his_creator(self):
        self.client.force_login(self.user)
        recipe_user = UserModel.objects.create_user(email='recipe@user.com', password='12345qwe')
        recipe = Recipe.objects.create(
            **self.VALID_RECIPE_DATA,
            created_by_id=recipe_user.id
        )
        response = self.client.get(reverse('recipe details', kwargs={
            'pk': recipe.id,
        }))
        self.assertFalse(response.context['is_creator'])

    def test_get_recipe_details__when__recipe_is_liked_and_user_not_is_creator__should_return_true(self):
        self.client.force_login(self.user)
        recipe_user = UserModel.objects.create_user(email='recipe@user.com', password='12345qwe')
        recipe = self.__create_recipe_with_like(
            like_user=self.user,
            recipe_name='Recipe',
            ingredients='first, second',
            recipe_picture='recipe.jpg',
            how_to_make='How to make',
            created_on=date.today(),
            category=Recipe.SOUPS,
            created_by=recipe_user
            )
        response = self.client.get(reverse('recipe details', kwargs={
            'pk': recipe.id,
        }))
        self.assertTrue(response.context['is_liked'])
        self.assertFalse(response.context['is_creator'])

    def test_get_recipe_details__when_recipe_is_liked_and_user_is_creator__should_be_true(self):
        self.client.force_login(self.user)

        recipe_user = UserModel.objects.create_user(email='recipe@user.com', password='12345qwe')
        recipe = self.__create_recipe_with_like(
            like_user=self.user,
            recipe_name='Recipe',
            ingredients='first, second',
            recipe_picture='recipe.jpg',
            how_to_make='How to make',
            created_on=date.today(),
            category=Recipe.SOUPS,
            created_by=self.user,
        )
        response = self.client.get(reverse('recipe details', kwargs={
            'pk': recipe.id,
        }))
        self.assertTrue(response.context['is_liked'])
        self.assertTrue(response.context['is_creator'])

