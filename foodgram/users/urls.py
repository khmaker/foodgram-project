from django.urls import path, include


from . import views

urlpatterns = [
    path('auth/signup/', views.SignUp.as_view(), name='signup'),
    path('auth/', include('django.contrib.auth.urls')),
]
