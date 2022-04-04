from django.urls import path

from recipes_app.main.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]