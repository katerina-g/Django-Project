from django import forms
from django.contrib.auth import forms as auth_forms
from django.urls import reverse_lazy
from django.views import generic as views

from final_project.accounts.models import FoodBlogUser, Profile


class UserRegistrationForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = FoodBlogUser
        fields = ('email',)

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(auth_forms.AuthenticationForm):
    pass


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'about_me': forms.Textarea(
                attrs={
                    'placeholder': 'Write something about you',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture', 'about_me',)


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

