from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users.models import User


class UserAdmin(DjangoUserAdmin):
    list_filter = ('username', 'email')


admin.site.register(User, UserAdmin)
