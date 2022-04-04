from django.urls import path

from final_project.food_app.views import HomeView, CommentRecipeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
    path('comment/<int:pk>', CommentRecipeView.as_view(), name='comment'),
    # path('home/', HomeFirstView.as_view(), name='home'),
)