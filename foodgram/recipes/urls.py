from django.urls import path

from recipes import views
from foodgram.views import about_tech
from foodgram.views import about_author


urlpatterns = [
    path('', views.RecipeListView.as_view(), name='index'),
    path('author/<str:username>/',
         views.AuthorListView.as_view(), name='author'),
    path('recipe/slug/<str:slug>/',
         views.RecipeView.as_view(), name='recipe_by_slug'),
    path('recipe/id/<int:pk>/',
         views.RecipeView.as_view(), name='recipe_by_id'),
    path('recipe/id/<int:pk>/edit/',
         views.RecipeEditView.as_view(), name='recipe_edit'),
    path('recipe/id/<int:pk>/delete/',
         views.RecipeDeleteView.as_view(), name='recipe_delete'),
    path('recipe/new/',
         views.RecipeCreateView.as_view(), name='new_recipe'),
    path('subscriptions/',
         views.FollowListView.as_view(), name='subscriptions'),
    path('favorites/',
         views.FavoritesListView.as_view(), name='favorites'),
    path('purchases/',
         views.PurchasesListView.as_view(), name='purchases'),
    path('about/author',
         about_author, name='about author'),
    path('about/tech',
         about_tech, name='about tech'),
]
