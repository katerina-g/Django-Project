from django.contrib.auth import mixins as auth_mixin
from django.contrib.auth import views as auth_views, login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from recipes_app.accounts.forms import UserRegistrationForm, LoginForm, CreateProfileForm
from recipes_app.accounts.models import Profile
from recipes_app.recipes.models import Recipe


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    authentication_form = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserLogoutView(views.TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


class CreateProfileView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/create_profile.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfileView(views.UpdateView):
    model = Profile
    fields = ('first_name', 'last_name', 'picture', 'about_me',)
    template_name = 'accounts/edit_profile.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class DeleteProfileView(views.DeleteView):
    template_name = 'accounts/delete_profile.html'
    model = Profile
    success_url = reverse_lazy('home')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = Recipe.objects.filter(created_by__profile=self.object.pk)
        context['recipes'] = recipes
        return context





