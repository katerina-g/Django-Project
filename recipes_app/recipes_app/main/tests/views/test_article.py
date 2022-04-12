from django.test import TestCase, Client

from django.contrib.auth import get_user_model
from django.urls import reverse

from recipes_app.main.models import Article

UserModel = get_user_model()


class ArticleTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@abv.bg',
        'password': '123456trewq',
        'is_superuser': True,
    }

    VALID_ARTICLE_DATA = {
        'title': 'Test',
        'text': 'test1 test2  test3',
        'picture': 'http://test.picture/url.png',
    }
    logged_in_user_email = 'test@abv.bg'
    logged_in_user_password = '123456trewq'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )

    def test_article_details__when_article_exists__expect_to_success(self):
        article = Article.objects.create(
            **self.VALID_ARTICLE_DATA,
            created_from=self.user
        )
        article.save()
        response = self.client.get(reverse('article details', kwargs={
            'pk': article.id,
        }))
        self.assertEqual(200, response.status_code)



