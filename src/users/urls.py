from django.urls import include
from django.urls import path

from users import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
