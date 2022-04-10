from django.test import TestCase
from datetime import date

from django.urls import reverse

from recipes_app.accounts.models import Profile, RecipesUser
from recipes_app.recipes.models import Recipe


class ProfileDetailsViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'Test',
    }

    VALID_RECIPE_DATA = {
        'recipe_name': 'Recipe',
        'ingredients': 'first, second',
        'recipe_picture': 'recipe.jpg',
        'how_to_make': 'How to make',
        'created_on': date.today(),
        'category': Recipe.SOUPS,
    }

    def __create_user(self, **credentials):
        return RecipesUser.objects.create(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return user, profile

    def __create_recipe_for_user_profile(self, user):
        recipe = Recipe.objects.create(
            **self.VALID_RECIPE_DATA,
            created_by_id=user.id
        )
        return recipe

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('profile details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/details.html')

    def test_when_user_has_no_recipes__recipes_should_be_empty(self):
        _, profile = self.__create_valid_user_and_profile()

        response = self.__get_response_for_profile(profile)
        self.assertListEqual([], list(response.context['recipes']))

    def test_when_user_has_recipes__expect_to_be_true(self):
        user, profile = self.__create_valid_user_and_profile()
        recipe = self.__create_recipe_for_user_profile(user)
        response = self.__get_response_for_profile(profile)
        self.assertEqual(1, len(response.context['recipes']))
        self.assertListEqual([recipe], list(response.context['recipes']))

    def test_when_user_has_recipes__expect_to_return_only_users_recipes(self):
        user, profile = self.__create_valid_user_and_profile()
        user2_credentials = {
            'email': 'test2@abv.bg',
            'password': '12345qwe',
        }
        profile2_credentials = {
            'first_name': 'Test2',
            'last_name': 'Test2',
        }
        recipe = self.__create_recipe_for_user_profile(user)
        user2 = self.__create_user(**user2_credentials)
        profile2 = Profile.objects.create(
            **profile2_credentials,
            user=user2,
        )
        recipe_2 = self.__create_recipe_for_user_profile(user2)

        response = self.__get_response_for_profile(profile)

        self.assertListEqual([recipe], list(response.context['recipes']))







