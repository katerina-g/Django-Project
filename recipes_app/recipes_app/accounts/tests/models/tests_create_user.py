from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserCreateTests(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }

    def test_user_create__when_data_is_valid__expect_success(self):
        user = UserModel(**self.VALID_USER_CREDENTIALS)
        user.save()
        self.assertIsNotNone(user.pk)

    def test_user_create__when_email__contains_only_letters__expect_to_fail(self):
        email = 'Test'
        user = UserModel(
            email=email,
            password=self.VALID_USER_CREDENTIALS['password'],
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)

    def test_user_create__when_password__contains_only_two_letters__expect_to_fail(self):
        password = '12'
        user = UserModel(
            email=self.VALID_USER_CREDENTIALS['password'],
            password=password,
        )

        with self.assertRaises(ValidationError) as context:
            user.full_clean()
            user.save()

        self.assertIsNotNone(context.exception)