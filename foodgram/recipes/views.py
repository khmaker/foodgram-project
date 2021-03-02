from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Follow, Recipe


class ProfileFollowView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        author = get_object_or_404(get_user_model(),
                                   username=self.kwargs['username'])
        if request.user != author:
            Follow.objects.get_or_create(user=request.user, author=author)
        return redirect('profile', username=self.kwargs['username'])


class ProfileUnfollowView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        author = get_object_or_404(get_user_model(),
                                   username=self.kwargs['username'])
        if request.user != author:
            Follow.objects.filter(user=request.user, author=author).delete()
        return redirect('profile', username=self.kwargs['username'])


class ProfileView(ListView):
    model = Recipe
    paginate_by = 6
    context_object_name = 'posts'
    template_name = 'profile.html'
    page_kwarg = 'page'
    user = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.user = request.user
        return super().dispatch(request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = get_object_or_404(get_user_model(),
                                   username=self.kwargs.get('username'))
        context['author'] = author
        context['following'] = Follow.objects.filter(user=self.user,
                                                     author=author).exists()
        return context
