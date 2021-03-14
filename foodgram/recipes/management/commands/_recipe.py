from random import choice, randint
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile as InMUF
from django.core.files import File


from recipes.models import Recipe, Tag, Ingredient, AmountOfIngredient
from users.models import User
from ._text_generator import TextLorem
from ._image_generator import generate_image


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
            recipe, created = create(author=author,
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
                recipe.image.save(title,
                                  InMUF(name=image_name,
                                        file=File(blob),
                                        field_name=None,
                                        content_type='image/jpeg',
                                        size=image.tell(),
                                        charset=None,
                                        ))

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
        AmountOfIngredient.objects.create(recipe=recipe,
                                          ingredient=choice(all_ingredients),
                                          amount=randint(1, 999), )
