from django.urls import path

from recipes import views


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='index'),
    path('<str:username>/',
         views.AuthorListView.as_view(), name='author'),
]
