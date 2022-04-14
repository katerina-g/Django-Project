from django.test import TestCase

from recipes_app.accounts.forms import UserRegistrationForm


class UserRegistrationFormTests(TestCase):
    def test_user_form_save__when_data_is_valid__expected_success(self):
        data = {
            'email': 'Test@abv.bg',
            'password1': '5678est123',
            'password2': '5678est123',
        }

        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())

    def test_user_form_save__when_data_is_invalid__expect_to_fail(self):
        data = {
            'email': 'Test@abv.bg',
            'password1': '5678est123',
            'password2': '5678est122',
        }
        form = UserRegistrationForm(data)
        self.assertFalse(form.is_valid())