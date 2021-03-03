from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Recipe, Tag


class RecipeListView(ListView):
    template_name = 'index.html'
    model = Recipe
    paginate_by = 6
    tags = Tag.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        tags_to_show = self.request.GET.getlist('tags')
        return (queryset.filter(tags__slug__in=tags_to_show).distinct()
                if tags_to_show else queryset)


class AuthorListView(RecipeListView):

    def get_queryset(self):
        author = get_object_or_404(get_user_model(),
                                   username=self.kwargs['username'])
        self.queryset = self.model.objects.filter(author=author)
        return super().get_queryset()
