from django.db.models import (Model, ForeignKey, CharField, SlugField,
                              ImageField, TextField, ManyToManyField,
                              PositiveSmallIntegerField, DateTimeField,
                              TextChoices, CASCADE,
                              )

from users.models import User


class Follow(Model):
    user = ForeignKey(User,
                      on_delete=CASCADE,
                      related_name='follower',
                      verbose_name='Подписчик', )
    author = ForeignKey(User,
                        on_delete=CASCADE,
                        related_name='following',
                        verbose_name='Подписки', )

    class Meta:
        unique_together = ['user', 'author']


class Ingredient(Model):
    title = CharField(max_length=100,
                      verbose_name='название ингредиента', )
    unit = CharField(max_length=64,
                     verbose_name='единица измерения', )

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'
        ordering = ['title']

    def __str__(self):
        return self.title


class Tag(Model):

    class Color(TextChoices):
        green = 'green'
        orange = 'orange'
        purple = 'purple'

    title = CharField(max_length=100,
                      verbose_name='имя тега', )
    slug = SlugField(null=False, unique=True)
    color = CharField(max_length=30,
                      choices=Color.choices,
                      default=Color.green)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title


class Recipe(Model):
    author = ForeignKey(User,
                        on_delete=CASCADE,
                        related_name='author',
                        verbose_name='автор', )
    title = CharField(max_length=200,
                      blank=False,
                      verbose_name='название', )
    image = ImageField(upload_to='recipe_pics/',
                       blank=True,
                       null=True,
                       help_text='Здесь можно загрузить картинку',
                       verbose_name='картинка', )
    description = TextField(verbose_name='текстовое описание', )
    ingredients = ManyToManyField(Ingredient,
                                  through='AmountOfIngredients',
                                  related_name='recipe_ingredient',
                                  verbose_name='ингредиенты', )
    tags = ManyToManyField(Tag,
                           related_name='tags',
                           verbose_name='тег', )
    cook_time = PositiveSmallIntegerField(verbose_name='время приготовления', )
    pub_date = DateTimeField(auto_now_add=True,
                             db_index=True,
                             verbose_name='дата публикации', )
    slug = SlugField(max_length=100,
                     unique=True,
                     default=None,
                     null=True,
                     verbose_name='уникальная часть URL для рецепта', )

    class Meta:
        ordering = ('-pub_date', 'title',)
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return self.title


class AmountOfIngredients(Model):
    amount = PositiveSmallIntegerField(verbose_name='количество ингредиента')
    recipe = ForeignKey(Recipe,
                        on_delete=CASCADE,
                        related_name='amount', )
    ingredient = ForeignKey(Ingredient,
                            on_delete=CASCADE,
                            related_name='amount', )

    class Meta:
        verbose_name = 'количество ингридиентов'
        unique_together = ['recipe', 'ingredient']

    def __str__(self):
        return f'{self.ingredient.title}: {self.amount} {self.ingredient.unit}'
