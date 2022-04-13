from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from recipes_app.accounts.models import Profile
from recipes_app.main.models import Comment
from recipes_app.recipes.models import Recipe

UserModel = get_user_model()


class CommentRecipeViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'test',
        'last_name': 'test',
    }
    VALID_RECIPE_DATA = {
        'recipe_name': 'Recipe',
        'ingredients': 'first, second',
        'recipe_picture': 'recipe.jpg',
        'how_to_make': 'How to make',
        'category': Recipe.SOUPS,
    }
    VALID_COMMENT_DATA = {
        'text_comment': 'Comment',
    }

    def test_create_comment__when_all_valid__expect_to_create_comment(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        user.save()
        recipe = Recipe(**self.VALID_RECIPE_DATA, created_by=user)
        recipe.save()
        self.client.force_login(user)
        Comment.objects.create(
            text_comment='Comment',
            user=user,
            recipe=recipe,
        )

        comment = Comment.objects.first()
        self.assertIsNotNone(comment)
        self.assertEqual(self.VALID_COMMENT_DATA['text_comment'], comment.text_comment)

    def test_post_comment__when_data_is_valid__expect_to_redirect_to_recipe_details(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        user.save()
        recipe = Recipe(**self.VALID_RECIPE_DATA, created_by=user)
        recipe.save()
        self.client.force_login(user)
        response = self.client.post(
            reverse('comment', kwargs={'pk': recipe.id}),
            data=self.VALID_COMMENT_DATA,
            recipe=recipe,
            user=user,
        )

        expected_url = reverse('recipe details', kwargs={'pk': recipe.pk})
        self.assertRedirects(response, expected_url)
