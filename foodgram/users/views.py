from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import CreationForm


class SignUp(CreateView):

    form_class = CreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/registration.html'

    def form_valid(self, form):
        """Log user in if all is ok"""
        is_valid = super().form_valid(form)
        login(self.request, self.object)
        return is_valid
