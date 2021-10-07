# coding=utf-8
from random import choice

from recipes.management.commands._text_generator import TextLorem
from recipes.models import Tag


def add_tags():
    create = Tag.objects.get_or_create
    word_generator = TextLorem(wsep='_', send='', srange=(1, 2))
    for _ in range(10):
        word = word_generator.word()
        color = choice(Tag.Color.values)
        try:
            tag, created = create(
                title=word,
                slug=word,
                color=color,
            )
            if created:
                tag.save()
        except Exception as e:
            print(e)
