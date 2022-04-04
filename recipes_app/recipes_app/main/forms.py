from django import forms

from recipes_app.main.models import Comment


class CommentRecipeForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_comment']
        widgets = {
            'text_comment': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Your Comment',
                }
            ),
        }