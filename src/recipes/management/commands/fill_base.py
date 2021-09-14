from django.core.management.base import BaseCommand

from ._users import add_users
from ._tags import add_tags
from ._recipe import add_recipe
from ._ingredient import add_ingredients


class Command(BaseCommand):

    def handle(self, *args, **options):
        add_users()
        add_tags()
        add_ingredients()
        add_recipe()
