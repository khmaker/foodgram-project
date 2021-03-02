from django.conf import settings
from django.conf.urls import handler404, handler500
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from foodgram import views

handler404 = 'foodgram.views.page_not_found'  # noqa
handler500 = 'foodgram.views.server_error'  # noqa

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
