from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import generic as views

from final_project.food_app.forms import CommentRecipeForm
from final_project.food_app.models import Comment
from final_project.recipes.models import Recipe, Like


class HomeView(views.TemplateView):
    context = {}
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all().order_by('-created_on')
        liked_recipes = Like.objects.all()
        categories = Recipe.CATEGORIES
        self.context['recipes'] = recipes
        self.context['liked_recipes'] = liked_recipes
        self.context['categories'] = categories
        return render(request, self.template_name, self.context)


class CommentRecipeView(LoginRequiredMixin, views.View):
    form_class = CommentRecipeForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            text_comment=form.cleaned_data['text_comment'],
            recipe=recipe,
            user=self.request.user,
        )
        comment.save()

        return redirect('recipe details', recipe.id)

    def form_invalid(self, form):
        pass
