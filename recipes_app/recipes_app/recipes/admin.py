from django.contrib import admin


from recipes_app.recipes.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe_name', 'ingredients', 'recipe_picture', 'how_to_make','category', 'created_on', 'created_by')
    