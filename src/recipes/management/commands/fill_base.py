# coding=utf-8
from django.core.management.base import BaseCommand

from recipes.management.commands._ingredient import add_ingredients
from recipes.management.commands._recipe import add_recipe
from recipes.management.commands._tags import add_tags
from recipes.management.commands._users import add_users


class Command(BaseCommand):

    def handle(self, *args, **options):
        add_users()
        add_tags()
        add_ingredients()
        add_recipe()
