from ._text_generator import TextLorem

from users.models import User


def add_users():
    create = User.objects.get_or_create
    name_generator = TextLorem(wsep='_', send='', srange=(1, 2))
    for i in range(1, 10):
        try:
            name = name_generator.sentence()
            user, created = create(username=name)
            if created:
                user.save()
        except Exception as e:
            print(e)
