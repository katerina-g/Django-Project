from django import forms

from final_project.food_app.models import Comment


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