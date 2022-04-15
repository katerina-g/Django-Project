from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse, reverse_lazy

from recipes_app.accounts.models import Profile

from recipes_app.recipes.models import Recipe

UserModel = get_user_model()


class TestHomeView(TestCase):
    VALID_ARTICLE_DATA = {
        'title': 'Test',
        'text': 'test1 test2  test3',
        'picture': 'cat.jpg',
    }

    VALID_RECIPE_DATA = {
        'recipe_name': 'Recipe',
        'ingredients': 'first, second',
        'recipe_picture': 'recipe.jpg',
        'how_to_make': 'How to make',
        'category': Recipe.SOUPS,
    }
    VALID_PROFILE_DATA = {
        'first_name': 'test',
        'last_name': 'test',
    }

    logged_in_user_email = 'test@abv.bg'
    logged_in_user_password = '123456trewq'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )

    def test_create_recipe__when_user_is_not_logged_in__expect_to_redirect_to_login(self):
        response = self.client.get(reverse('create recipe'))
        self.assertEqual(302, response.status_code)

    def test_create_recipe__when_user_is_logged_and_have_no_profile__expect_to_redirect_to_create_profile(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create recipe'))
        self.assertEqual(302, response.status_code)
        self.assertEqual('/accounts/create_profile/', response.url)

    def test_create_recipe__when_user_is_logged_and_have_profile__expect_to_open_create_recipe(self):
        self.client.force_login(self.user)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=self.user,
        )
        profile.save()
        response = self.client.get(reverse('create recipe'))
        self.assertEqual(200, response.status_code)

    def test_get_home__when_user_is_logged(self):
        self.client.force_login(self.user)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=self.user,
        )
        profile.save()
        recipes_to_create = (
            Recipe(recipe_name='recipe', ingredients='one, two', recipe_picture='recipe.jpg', how_to_make='blabla',
                   created_by=self.user, category=Recipe.SOUPS),
            Recipe(recipe_name='recipe2', ingredients='one, two', recipe_picture='recipe.jpg', how_to_make='blabla',
                   created_by=self.user, category=Recipe.SOUPS),
            Recipe(recipe_name='recipe3', ingredients='one, two', recipe_picture='recipe.jpg', how_to_make='blabla',
                   created_by=self.user, category=Recipe.SOUPS)
        )
        Recipe.objects.bulk_create(recipes_to_create)
        response = self.client.get(reverse_lazy('home'))
        recipes = response.context['recipes']
        liked_recipes = response.context['liked_recipes']
        profiles = response.context['profiles']
        self.assertEqual(len(recipes), 3)
        self.assertEqual(len(liked_recipes), 0)
        self.assertEqual(len(profiles), 1)

