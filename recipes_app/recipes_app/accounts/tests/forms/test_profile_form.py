from django.test import TestCase

from recipes_app.accounts.forms import CreateProfileForm


class ProfileFormTests(TestCase):
    def test_profile_form_save__when_data_is_valid__expected_success(self):
        data = {
            'first_name': 'Test',
            'last_name': 'Test',
        }
        form = CreateProfileForm(data)
        self.assertTrue(form.is_valid())

    def test_profile_form_save__when_data_is_invalid__expect_to_fail(self):
        data = {
            'first_name': 'Test',
            'last_name': '',
        }
        form = CreateProfileForm(data)
        self.assertFalse(form.is_valid())