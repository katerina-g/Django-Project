import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from recipes_app.main.forms import ArticleForm
from django.conf import settings


class ArticleFormTests(TestCase):
    def test_article_form_save__when_data_is_invalid__expect_to_fail(self):
        data = {
            'title': 'Test',
            'text': 'test1 test2  test3',
            'picture': 'http://test.picture/url.png',
        }
        form = ArticleForm(data)
        self.assertFalse(form.is_valid())

    def test_article_form_save__when_data_is_valid__expect_to_be_true(self):
        file_path = os.path.join(settings.BASE_DIR, 'recipes_app/recipes/tests/cat.jpg')
        data = {
            'title': 'Test',
            'text': 'test1 test2  test3',
        }

        with open(file_path, 'rb') as f:
            form = ArticleForm(data=data, files={'picture': SimpleUploadedFile('cat.jpg', f.read())})
            self.assertTrue(form.is_valid())