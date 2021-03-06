from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Recipe, Tag
from users.models import User


class RecipeListView(ListView):
    template_name = 'index.html'
    model = Recipe
    paginate_by = 6

    def __init__(self, **kwargs):
        self.author = None
        self.counter = None
        self.tags = Tag.objects.all()
        super().__init__(**kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            self.counter = user.purchases.all().count
        tags_to_show = self.request.GET.getlist('tags')
        self.tags = Tag.objects.filter(recipes__in=queryset).distinct()
        return (queryset.filter(tags__slug__in=tags_to_show).distinct()
                if tags_to_show else queryset)


class AuthorListView(RecipeListView):

    def get_queryset(self):
        queryset = super().get_queryset()
        self.author = get_object_or_404(User,
                                        username=self.kwargs.get('username'))
        self.tags = Tag.objects.filter(recipes__author=self.author).distinct()
        queryset = queryset.filter(author=self.author)
        return queryset


class RecipeView(DetailView):
    model = Recipe
    template_name = 'single_recipe.html'


class FollowListView(LoginRequiredMixin, ListView):
    template_name = 'follow.html'
    paginate_by = 3

    def get_queryset(self):
        return User.objects.filter(following__user=self.request.user)


class FavoritesListView(LoginRequiredMixin, RecipeListView):

    def get_queryset(self):
        queryset = Recipe.objects.filter(favorites__user=self.request.user)
        self.queryset = queryset
        return super().get_queryset()


class PurchasesListView(LoginRequiredMixin, RecipeListView):
    template_name = 'shopList.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        queryset = self.request.user.purchases.all()
        self.counter = queryset.count
        return queryset
