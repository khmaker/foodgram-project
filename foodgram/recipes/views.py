import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Recipe, Tag, Follow
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


class FollowListView(LoginRequiredMixin, ListView):
    template_name = 'follow.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = User.objects.filter(following__user=self.request.user)
        return queryset

    def post(self, request):
        r = json.loads(request.body)
        author_id = r.get('id')
        if author_id is not None:
            author = get_object_or_404(User, id=author_id)
            obj, created = Follow.objects.get_or_create(user=request.user,
                                                        author=author, )
            return JsonResponse({'success': created})
        return JsonResponse({'success': False}, status=400)

    def delete(self, request, author_id):
        author = get_object_or_404(Follow, user=request.user, author=author_id)
        author.delete()
        success = not request.user.follower.filter(author=author_id).exists()
        return JsonResponse({'success': success})
