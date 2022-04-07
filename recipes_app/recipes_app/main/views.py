from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from recipes_app.accounts.models import Profile
from recipes_app.main.forms import CommentRecipeForm, ArticleForm
from recipes_app.main.models import Like, Comment, Article
from recipes_app.recipes.models import Recipe


class HomeView(views.TemplateView):
    context = {}
    template_name = 'base/home.html'

    def get(self, request, *args, **kwargs):
        recipes = Recipe.objects.all().order_by('-created_on')
        liked_recipes = Like.objects.all()
        profiles = Profile.objects.all()
        categories = Recipe.CATEGORIES
        articles = Article.objects.all().order_by('-date_created')
        self.context['recipes'] = recipes
        self.context['liked_recipes'] = liked_recipes
        self.context['profiles'] = profiles
        self.context['categories'] = categories
        self.context['articles'] = articles
        return render(request, self.template_name, self.context)


class LikeRecipeView(LoginRequiredMixin, views.View):
    def get(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = recipe.like_set.filter(user_id=self.request.user.id) \
            .first()
        if like_object_by_user:
            like_object_by_user.delete()
        else:
            like = Like(
                recipe=recipe,
                user=self.request.user,
            )
            like.save()
        return redirect('recipe details', recipe.pk)


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


class CreateArticleView(LoginRequiredMixin, views.CreateView):
    form_class = ArticleForm
    template_name = 'base/create_article.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.created_from = self.request.user
        article.save()
        return super().form_valid(form)


class ArticleDetailsView(views.DetailView):
    model = Article
    template_name = 'base/article_details.html'
    context_object_name = 'article'