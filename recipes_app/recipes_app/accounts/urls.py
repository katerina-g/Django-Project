from django.urls import path

from recipes_app.accounts.views import UserRegistrationView, UserLoginView, UserLogoutView, CreateProfileView, \
    EditProfileView, DeleteProfileView, ProfileDetailsView, ProfilesListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('create_profile/', CreateProfileView.as_view(), name='create profile'),
    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('delete_profile/<int:pk>/', DeleteProfileView.as_view(), name='delete profile'),
    path('details/<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('all_profiles/', ProfilesListView.as_view(), name='profiles list'),
]