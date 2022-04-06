from django.db import models
from django.contrib.auth import get_user_model

from recipes_app.accounts.models import Profile
from recipes_app.recipes.models import Recipe

UserModel = get_user_model()


class Comment(models.Model):
    text_comment = models.TextField()
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


# class Article(models.Model):
#     TITLE_MAX_LENGTH = 35
#     TEXT_MAX_LENGTH = 1200
#
#     title = models.CharField(
#         max_length=TITLE_MAX_LENGTH,
#     )
#     text = models.CharField(
#         max_length=TEXT_MAX_LENGTH,
#     )
#     created_from = models.ForeignKey(
#         UserModel,
#         on_delete=models.CASCADE
#     )
#     date_created = models.DateTimeField(
#         auto_now_add=True,
#     )
