from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from recipes_app.main.models import Article

UserModel = get_user_model()


class ArticleModelTest(TestCase):
    VALID_USER_DATA = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
    }

    VALID_ARTICLE_DATA = {
        'title': 'Test',
        'text': 'test1 test2  test3',
        'picture': 'http://test.picture/url.png',
    }

    def test_article_create__when_all_data_is_valid__expect_success(self):
        user = UserModel(**self.VALID_USER_DATA)
        user.save()
        article = Article(
            title=self.VALID_ARTICLE_DATA['title'],
            text=self.VALID_ARTICLE_DATA['text'],
            picture=self.VALID_ARTICLE_DATA['picture'],
            created_from_id=user.id
        )
        article.save()
        self.assertIsNotNone(article.pk)

    def test_article_create__when_article_picture_is_empty__expected_to_fail(self):
        user = UserModel(**self.VALID_USER_DATA)
        user.save()
        picture = ''
        article = Article(
            title=self.VALID_ARTICLE_DATA['title'],
            text=self.VALID_ARTICLE_DATA['text'],
            picture=picture,
            created_from_id=user.id
        )
        with self.assertRaises(ValidationError) as context:
            article.full_clean()
            article.save()

        self.assertIsNotNone(context.exception)