from random import choice, randint
from io import BytesIO

from django.core.files.uploadedfile import InMemoryUploadedFile as InMUF
from django.core.files import File


from recipes.models import Recipe, Tag
from users.models import User
from ._text_generator import TextLorem
from ._image_generator import generate_image


def add_recipe():
    all_users = User.objects.all()
    all_tags = Tag.objects.all()
    create = Recipe.objects.get_or_create
    text_generator = TextLorem()
    sentence_generator = TextLorem(send='', srange=(1, 2))
    for user_object in all_users:
        number_of_recipes = randint(1, 10)
        for _ in range(number_of_recipes):
            try:
                author = user_object
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
                    recipe.save()
            except Exception as e:
                print(e)
