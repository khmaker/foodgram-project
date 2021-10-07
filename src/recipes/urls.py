# coding=utf-8
from django.urls import path

from foodgram.views import about_author, about_tech
from recipes.views import (
    AuthorListView, FavoritesListView, FollowListView, PurchasesListView,
    RecipeCreateView, RecipeDeleteView, RecipeEditView, RecipeListView,
    RecipeView,
)

urlpatterns = [
    path('', RecipeListView.as_view(), name='index'),
    path(
        'author/<str:username>/',
        AuthorListView.as_view(), name='author'
        ),
    path(
        'recipe/slug/<str:slug>/',
        RecipeView.as_view(), name='recipe_by_slug'
        ),
    path(
        'recipe/id/<int:pk>/',
        RecipeView.as_view(), name='recipe_by_id'
        ),
    path(
        'recipe/id/<int:pk>/edit/',
        RecipeEditView.as_view(), name='recipe_edit'
        ),
    path(
        'recipe/id/<int:pk>/delete/',
        RecipeDeleteView.as_view(), name='recipe_delete'
        ),
    path(
        'recipe/new/',
        RecipeCreateView.as_view(), name='new_recipe'
        ),
    path(
        'subscriptions/',
        FollowListView.as_view(), name='subscriptions'
        ),
    path(
        'favorites/',
        FavoritesListView.as_view(), name='favorites'
        ),
    path(
        'purchases/',
        PurchasesListView.as_view(), name='purchases'
        ),
    path(
        'about/author',
        about_author, name='about author'
        ),
    path(
        'about/tech',
        about_tech, name='about tech'
        ),
]
