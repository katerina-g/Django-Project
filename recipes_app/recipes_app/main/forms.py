from django import forms

from recipes_app.main.models import Comment, Article


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


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'picture']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Article Title',
                }
            ),
            'text': forms.Textarea(
                attrs={
                    'placeholder': 'Article Text'
                }
            ),
            'picture': forms.FileInput()
        }