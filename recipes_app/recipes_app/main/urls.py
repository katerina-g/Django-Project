from django.urls import path

from recipes_app.main.views import HomeView, CommentRecipeView, LikeRecipeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('comment/<int:pk>', CommentRecipeView.as_view(), name='comment'),
    path('like/<int:pk>/', LikeRecipeView.as_view(), name='like recipe'),
]