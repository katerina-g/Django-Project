from django.db import models

from django.db import models
from django.contrib.auth import models as auth_models

from final_project.accounts.managers import UsersManager


class FoodBlogUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    object = UsersManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
    )

    picture = models.URLField(
        blank=True,
        null=True,
    )
    about_me = models.TextField(
        blank=True,
        null=True,
    )
    user = models.OneToOneField(
        FoodBlogUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
