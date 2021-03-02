"""Users views"""

from django.views.generic import CreateView

from .forms import CreationForm


class SignUp(CreateView):
    """Signup view"""
    form_class = CreationForm
    success_url = '/auth/login/'
    template_name = 'registration/registration.html'
