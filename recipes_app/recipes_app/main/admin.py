from django.contrib import admin

from recipes_app.main.models import Comment, Like


@admin.register(Comment)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'user')