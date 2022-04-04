from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic as views

from recipes_app.recipes.models import Recipe


class HomeView(views.TemplateView):
    context = {}
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all().order_by('-created_on')
        # liked_recipes = Like.objects.all()
        categories = Recipe.CATEGORIES
        self.context['recipes'] = recipes
        # self.context['liked_recipes'] = liked_recipes
        self.context['categories'] = categories
        return render(request, self.template_name, self.context)
