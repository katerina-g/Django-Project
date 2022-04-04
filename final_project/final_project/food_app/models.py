from django.contrib.auth import get_user_model
from django.db import models

from final_project.recipes.models import Recipe

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


