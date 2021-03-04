from random import choice, randint

from recipes.models import Recipe, Tag
from users.models import User
from ._text_generator import TextLorem


def add_recipe():
    all_users = User.objects.all()
    all_tags = Tag.objects.all()
    create = Recipe.objects.get_or_create
    text_generator = TextLorem()
    for user_object in all_users:
        number_of_recipes = randint(1, 10)
        for _ in range(number_of_recipes):
            try:
                author = user_object
                title = text_generator.word()
                description = text_generator.paragraph()
                recipe, created = create(author=author,
                                         title=title,
                                         description=description,
                                         cook_time=1,
                                         slug=title,
                                         )
                if created:
                    for _ in range(randint(1, 5)):
                        tags = choice(all_tags)
                        recipe.tags.add(tags)
                    recipe.save()
            except Exception as e:
                print(e)
                raise e
