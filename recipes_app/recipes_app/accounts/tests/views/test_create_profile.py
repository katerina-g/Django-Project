from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from recipes_app.accounts.models import Profile
UserModel = get_user_model()


class ProfileCreateViewTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'test',
        'last_name': 'test',
    }

    def test_create_profile__when_all_valid__expect_to_create(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        user.save()
        self.client.force_login(user)
        self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
            user=user,
        )

        profile = Profile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)

    def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        user.save()
        self.client.force_login(user)
        response = self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
            user=user
        )

        profile = Profile.objects.first()

        expected_url = reverse('profile details', kwargs={'pk': profile.pk})
        self.assertRedirects(response, expected_url)
