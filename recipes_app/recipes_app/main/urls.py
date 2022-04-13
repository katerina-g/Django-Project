from django.urls import path

from recipes_app.main.views import HomeView, CommentRecipeView, LikeRecipeView, CreateArticleView, ArticleDetailsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('comment/recipe/<int:pk>', CommentRecipeView.as_view(), name='comment'),
    path('like/<int:pk>/', LikeRecipeView.as_view(), name='like recipe'),
    path('create_article/', CreateArticleView.as_view(), name='create article'),
    path('article_details/<int:pk>/', ArticleDetailsView.as_view(), name='article details'),
]