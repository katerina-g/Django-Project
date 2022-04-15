from django.contrib.auth import get_user_model

from django.test import TestCase
from django.urls import reverse

from recipes_app.accounts.models import RecipesUser


class RecipeUserRegisterViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password1': '123456trewq',
        'password2': '123456trewq',
    }

    def test_register_user__when_data_is_valid__expect_success(self):
        response = self.client.post(reverse('register'),
                                    data=self.VALID_USER_CREDENTIALS, )
        user = RecipesUser.objects.first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@abv.bg')
        expected_url = reverse('home')
        self.assertRedirects(response, expected_url)

    def test_register_user__when_data_is_not_valid__expect_fail(self):
        email = ''
        response = self.client.post(reverse('register'),
                                    email=email,
                                    password1=self.VALID_USER_CREDENTIALS['password1'],
                                    password2=self.VALID_USER_CREDENTIALS['password2'],
                                    )

        self.assertRaises(ValueError)

    def test_create_superuser(self):
        db = get_user_model()
        super_user = db.objects.create_superuser(
            email='test@abv.bg',
            password='123456trewq',
        )
        self.assertEqual(super_user.email, 'test@abv.bg')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
