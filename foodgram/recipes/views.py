from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Recipe, Tag
from users.models import User


class RecipeListView(ListView):
    template_name = 'index.html'
    model = Recipe
    paginate_by = 6

    def __init__(self, **kwargs):
        self.author = None
        self.tags = Tag.objects.all()
        super().__init__(**kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags_to_show = self.request.GET.getlist('tags')
        return (queryset.filter(tags__slug__in=tags_to_show).distinct()
                if tags_to_show else queryset)


class AuthorListView(RecipeListView):

    def get_queryset(self):
        queryset = super().get_queryset()
        self.author = get_object_or_404(User,
                                        username=self.kwargs.get('username'))
        queryset = queryset.filter(author=self.author)
        return queryset


class RecipeView(DetailView):
    model = Recipe
    template_name = 'single_recipe.html'
