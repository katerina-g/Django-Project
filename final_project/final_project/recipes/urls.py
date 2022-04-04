from django.urls import path

from final_project.recipes.views import CreateRecipesView, RecipeDetailsView, EditRecipeView, DeleteRecipeView, \
    ListRecipesView, LikeRecipeView, SaladsView, SoupsView, AppetizersView, MainDishesView, DessertsView, \
    BakedDishesView, OtherDishesView

urlpatterns = (
    path('create/', CreateRecipesView.as_view(), name='create recipe'),
    path('edit_recipe/<int:pk>/', EditRecipeView.as_view(), name='edit recipe'),
    path('details/<int:pk>/', RecipeDetailsView.as_view(), name='recipe details'),
    path('delete_recipe/<int:pk>', DeleteRecipeView.as_view(), name='delete recipe'),
    path('all_recipes', ListRecipesView.as_view(), name='all recipes'),
    path('like/<int:pk>/', LikeRecipeView.as_view(), name='like recipe'),
    path('salads/', SaladsView.as_view(), name='salads'),
    path('soups/', SoupsView.as_view(), name='soups'),
    path('appetizers/', AppetizersView.as_view(), name='appetizers'),
    path('main_dishes/', MainDishesView.as_view(), name='main_dishes'),
    path('desserts/', DessertsView.as_view(), name='desserts'),
    path('baked_dishes/', BakedDishesView.as_view(), name='baked dishes'),
    path('other/', OtherDishesView.as_view(), name='other'),
)