# coding=utf-8
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class CreationForm(UserCreationForm):
    password2 = None  # disabling password confirmation

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'username', 'email')
