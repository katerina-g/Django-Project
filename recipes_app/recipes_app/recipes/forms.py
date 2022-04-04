import os
from os.path import join

from django import forms
from django.conf import settings

from recipes_app.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['created_on', 'created_by', ]
        widgets = {
            'recipe_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Recipe Name',
                }
            ),
            'ingredients': forms.Textarea(
                attrs={
                    'placeholder': 'Enter Ingredients',
                }
            ),
            'recipe_picture': forms.FileInput(

            ),
            'how_to_make': forms.Textarea(
                attrs={
                    'placeholder': 'How To Make',
                }
            ),

        }


class EditRecipeForm(forms.ModelForm):
    def save(self, commit=True):
        db_recipe = Recipe.objects.get(pk=self.instance.id)
        if commit:
            image_path = join(settings.MEDIA_ROOT, str(db_recipe.recipe_picture))
            os.remove(image_path)
        return super().save(commit)

    class Meta:
        model = Recipe
        exclude = ['created_on', 'created_by', ]
        widgets = {
            'recipe_name': forms.TextInput(),
            'ingredients': forms.Textarea(),
            'recipe_picture': forms.FileInput(),
            'how_to_make': forms.Textarea(),
        }


class DeleteRecipeForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Recipe
        exclude = ['created_on', 'created_by', ]
