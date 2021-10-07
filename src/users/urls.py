# coding=utf-8
from django.urls import include, path

from users.views import SignUp

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
