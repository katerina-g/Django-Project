from django.contrib import admin

from recipes_app.accounts.models import Profile, RecipesUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(RecipesUser)
class RecipesUserAdmin(admin.ModelAdmin):
    pass