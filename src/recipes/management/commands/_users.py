# coding=utf-8
import names

from users.models import User


def add_users():
    create = User.objects.get_or_create
    for _ in range(10):
        try:
            name = names.get_full_name()
            user, created = create(
                username=name,
                email=name + '@example.com',
            )
            if created:
                user.save()
        except Exception as e:
            print(e)
