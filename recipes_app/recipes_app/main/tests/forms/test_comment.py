from django.test import TestCase

from recipes_app.main.forms import CommentRecipeForm


class CommentFormTests(TestCase):
    def test_comment_form_save__when_data_is_invalid__expect_to_be_true(self):
        data = {
            'text_comment': 'Test',
        }
        form = CommentRecipeForm(data)
        self.assertTrue(form.is_valid())

    def test_comment_form_save__when_data_is_invalid__expect_to_fail(self):
        data = {
            'text_comment': '',
        }
        form = CommentRecipeForm(data)
        self.assertFalse(form.is_valid())