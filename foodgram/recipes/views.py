from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from users.models import User
from recipes.forms import RecipeForm
from recipes.models import Recipe
from recipes.models import Tag


class BaseListView(ListView):
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
        self.tags = Tag.objects.filter(recipes__in=queryset).distinct()
        return (queryset.filter(tags__slug__in=tags_to_show).distinct()
                if tags_to_show else queryset)


class RecipeListView(BaseListView):

    def get_queryset(self):
        return super().get_queryset()


class AuthorListView(BaseListView):

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


class FavoritesListView(LoginRequiredMixin, BaseListView):

    def get_queryset(self):
        queryset = Recipe.objects.filter(favorites__user=self.request.user)
        self.queryset = queryset
        return super().get_queryset()


class PurchasesListView(LoginRequiredMixin, BaseListView):
    template_name = 'shop_list.html'
    context_object_name = 'purchases'

    def get_queryset(self):
        queryset = self.request.user.purchases.all()
        return queryset


class RecipeCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'recipe_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeEditView(LoginRequiredMixin, UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name = 'recipe_form.html'

    def get(self, request, *args, **kwargs):
        self.recipe = self.get_object()
        if request.user != self.recipe.author:
            return redirect(self.recipe.get_absolute_url())
        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        return super().form_invalid(form=form)


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('index')
    template_name = 'recipe_confirm_delete.html'
    pk_url_kwarg = 'pk'
