# coding=utf-8
from io import BytesIO
from random import choice, randint

from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile as InMUF

from recipes.management.commands._image_generator import generate_image
from recipes.management.commands._text_generator import TextLorem
from recipes.models import AmountOfIngredient, Ingredient, Recipe, Tag
from users.models import User


def add_recipe():
    all_users = User.objects.all()
    all_tags = Tag.objects.all()
    create = Recipe.objects.get_or_create
    text_generator = TextLorem()
    sentence_generator = TextLorem(send='', srange=(2, 4))
    for _ in range(100):
        try:
            author = choice(all_users)
            title = sentence_generator.sentence()
            description = text_generator.text()
            cook_time = randint(0, 1000)
            recipe, created = create(
                author=author,
                title=title,
                description=description,
                cook_time=cook_time,
                slug=title,
            )
            if created:
                image = generate_image()
                image_name = f'{title}' + '.jpeg'
                blob = BytesIO()
                image.save(blob, 'JPEG')
                recipe.image.save(
                    title,
                    InMUF(
                        name=image_name,
                        file=File(blob),
                        field_name=None,
                        content_type='image/jpeg',
                        size=image.tell(),
                        charset=None,
                    )
                )

                for _ in range(randint(1, 5)):
                    tags = choice(all_tags)
                    recipe.tags.add(tags)
                add_ingredients_to_recipe(recipe)
                recipe.save()
        except Exception as e:
            print(e)


def add_ingredients_to_recipe(recipe):
    all_ingredients = Ingredient.objects.all()
    for _ in range(randint(1, 5)):
        AmountOfIngredient.objects.create(
            recipe=recipe,
            ingredient=choice(all_ingredients),
            amount=randint(1, 999),
        )
