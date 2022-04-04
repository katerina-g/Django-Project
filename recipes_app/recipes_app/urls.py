from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes_app.main.urls')),
    path('accounts/', include('recipes_app.accounts.urls')),
    path('recipes/', include('recipes_app.recipes.urls')),
]
