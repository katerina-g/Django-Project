from django.db import models

from recipes_app.accounts.models import RecipesUser
from recipes_app.recipes.validators import validate_ingredients, validate_picture_max_size


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
    ingredients = models.TextField(
        max_length=500,
        verbose_name='Ingredients',
        validators=(validate_ingredients,),
    )
    recipe_picture = models.ImageField(
        verbose_name='Recipe Picture',
        upload_to="mediafiles",
        validators=(
            validate_picture_max_size,
        )
    )
    how_to_make = models.TextField(
        max_length=800,
        verbose_name='How To Make'
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        RecipesUser,
        on_delete=models.CASCADE,
    )
    category = models.CharField(
        max_length=max(len(x) for (x, _) in CATEGORIES),
        verbose_name='Category',
        choices=CATEGORIES,
    )

    def __str__(self):
        return f'{self.recipe_name}'
