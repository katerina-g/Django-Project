from django.contrib.auth import get_user_model
from django.db import models

from final_project.accounts.models import FoodBlogUser
from final_project.recipes.validators import validate_ingredients

UserModel = get_user_model()


class Recipe(models.Model):
    SALADS = 'Salads'
    SOUPS = 'Soups'
    APPETIZERS = 'Appetizers'
    MAIN_DISHES = 'Main dishes'
    DESSERTS = 'Desserts'
    BAKED_DISHES = 'Baked dishes'
    OTHER = 'Other'

    CATEGORIES = [(x, x) for x in (SALADS, SOUPS, APPETIZERS, MAIN_DISHES, DESSERTS, BAKED_DISHES, OTHER)]
    recipe_name = models.CharField(
        max_length=100,
        verbose_name='Recipe Name',
    )
    ingredients = models.CharField(
        max_length=500,
        verbose_name='Ingredients',
        validators=(validate_ingredients,),
    )
    recipe_picture = models.ImageField(
        verbose_name='Recipe Picture',
        upload_to="mediafiles",
    )
    how_to_make = models.CharField(
        max_length=800,
        verbose_name='How To Make'
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        FoodBlogUser,
        on_delete=models.CASCADE,
    )
    category = models.CharField(
        max_length=max(len(x) for (x, _) in CATEGORIES),
        verbose_name='Category',
        choices=CATEGORIES,
    )

    def __str__(self):
        return f'{self.recipe_name}'


class Like(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
