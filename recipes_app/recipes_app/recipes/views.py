from django.contrib.auth import mixins as auth_mixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from recipes_app.accounts.models import Profile
from recipes_app.main.forms import CommentRecipeForm
from recipes_app.main.models import Comment
from recipes_app.main.view_mixin import RedirectToCreateProfile
from recipes_app.recipes.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from recipes_app.recipes.models import Recipe


class CreateRecipesView(auth_mixin.LoginRequiredMixin, RedirectToCreateProfile, views.CreateView):
    form_class = CreateRecipeForm
    template_name = 'recipes/create.html'

    def get_success_url(self):
        return reverse_lazy('recipe details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.created_by = self.request.user
        recipe.save()
        return super().form_valid(form)


class EditRecipeView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Recipe
    template_name = 'recipes/edit_recipe.html'
    form_class = EditRecipeForm

    def get_success_url(self):
        return reverse_lazy('recipe details', kwargs={'pk': self.object.pk})


class DeleteRecipeView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Recipe
    form_class = DeleteRecipeForm
    template_name = 'recipes/delete_recipe.html'

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.request.user.id})


class RecipeDetailsView(views.DetailView):
    model = Recipe
    template_name = 'recipes/details.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = context['recipe']

        recipe_ingredients = recipe.ingredients.split(', ')
        recipe.likes_count = recipe.like_set.count()
        is_creator = recipe.created_by_id == self.request.user.id
        is_liked_by_user = recipe.like_set.filter(user_id=self.request.user.id).exists()
        user_profile = Profile.objects.filter(user_id=self.request.user.id).exists()
        context['comment_form'] = CommentRecipeForm(
            initial={
                'recipe_pk': self.object.pk,
            }
        )
        context['comments'] = Comment.objects.all()
        context['is_creator'] = is_creator
        context['recipe_ingredients'] = recipe_ingredients
        context['is_liked'] = is_liked_by_user
        context['user_profile'] = user_profile
        return context


class ListRecipesView(views.ListView):
    template_name = 'recipes/all_recipes.html'
    context_object_name = 'recipes'
    model = Recipe
    ordering = ['-created_on']


class SaladsView(views.TemplateView):
    context = {}
    template_name = 'recipes/salads.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        salads = recipes.filter(category='Salads')
        self.context['recipes'] = recipes
        self.context['salads'] = salads
        return render(request, self.template_name, self.context)


class SoupsView(views.TemplateView):
    context = {}
    template_name = 'recipes/soups.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        soups = recipes.filter(category='Soups')
        self.context['recipes'] = recipes
        self.context['soups'] = soups
        return render(request, self.template_name, self.context)


class AppetizersView(views.TemplateView):
    context = {}
    template_name = 'recipes/appetizers.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        appetizers = recipes.filter(category='Appetizers')
        self.context['recipes'] = recipes
        self.context['appetizers'] = appetizers
        return render(request, self.template_name, self.context)


class MainDishesView(views.TemplateView):
    context = {}
    template_name = 'recipes/main_dishes.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        main_dishes = recipes.filter(category='Main dishes')
        self.context['recipes'] = recipes
        self.context['main_dishes'] = main_dishes
        return render(request, self.template_name, self.context)


class DessertsView(views.TemplateView):
    context = {}
    template_name = 'recipes/desserts.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        desserts = recipes.filter(category='Desserts')
        self.context['recipes'] = recipes
        self.context['desserts'] = desserts
        return render(request, self.template_name, self.context)


class BakedDishesView(views.TemplateView):
    context = {}
    template_name = 'recipes/baked_dishes.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        baked_dishes = recipes.filter(category='Baked dishes')
        self.context['recipes'] = recipes
        self.context['baked_dishes'] = baked_dishes
        return render(request, self.template_name, self.context)


class OtherDishesView(views.TemplateView):
    context = {}
    template_name = 'recipes/other.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all()
        other = recipes.filter(category='Other')
        self.context['recipes'] = recipes
        self.context['other'] = other
        return render(request, self.template_name, self.context)