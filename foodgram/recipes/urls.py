from django.urls import path

from recipes import views


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='index'),
]
