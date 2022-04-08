from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from recipes_app.accounts.models import Profile

UserModel = get_user_model()


class ProfileCreateTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'Test',
    }

    def test_profile_create__when_first_and_last_name__contains_only_letters__expect_success(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        profile = Profile(
            **self.VALID_PROFILE_DATA,
            user=user
        )
        user.save()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name__contains_a_digit__expect_to_fail(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        first_name = 'Test1'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            user=user
        )
        user.save()

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name__contains_a_digit__expect_to_fail(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        last_name = 'Test1'
        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=last_name,
            user=user
        )
        user.save()

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_and_last_name__contains_a_digit__expect_to_fail(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        first_name = 'Test1'
        last_name = 'Test1'
        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            user=user
        )
        user.save()

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name__contains_a_space__expect_to_fail(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        last_name = 'T est'
        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=last_name,
            user=user
        )
        user.save()

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name__contains_a_underscore__expect_to_fail(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        first_name = 'Test_'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            user=user
        )
        user.save()

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)