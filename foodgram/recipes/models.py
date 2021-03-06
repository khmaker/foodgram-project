from django.db.models import (Model, ForeignKey, CharField, SlugField,
                              ImageField, TextField, ManyToManyField,
                              PositiveSmallIntegerField, DateTimeField,
                              TextChoices, CASCADE, )
from django.dispatch import receiver
from django.db.models.signals import post_delete

from django.urls import reverse

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
                        related_name='recipes',
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
                           related_name='recipes',
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

    def get_absolute_url(self):
        slug = self.slug
        if slug is not None:
            return reverse('recipe_by_slug',
                           kwargs={'slug': self.slug})
        return reverse('recipe_by_id',
                       kwargs={'pk': self.id})


@receiver(post_delete, sender=Recipe)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class AmountOfIngredients(Model):
    amount = PositiveSmallIntegerField(verbose_name='количество ингредиента')
    recipe = ForeignKey(Recipe,
                        on_delete=CASCADE,
                        related_name='amount', )
    ingredient = ForeignKey(Ingredient,
                            on_delete=CASCADE,
                            related_name='amount', )

    class Meta:
        verbose_name = 'количество ингредиентов'
        unique_together = ['recipe', 'ingredient']

    def __str__(self):
        return f'{self.ingredient.title}: {self.amount} {self.ingredient.unit}'


class Favorite(Model):
    user = ForeignKey(User,
                      on_delete=CASCADE,
                      related_name='favorites', )
    recipe = ForeignKey(Recipe,
                        on_delete=CASCADE,
                        related_name='favorites', )

    class Meta:
        verbose_name = 'избранное'
        unique_together = ['user', 'recipe']

    def __str__(self):
        return f'{self.user}-{self.recipe}'


class Purchase(Model):
    user = ForeignKey(User,
                      on_delete=CASCADE,
                      related_name='purchases',
                      verbose_name='Пользователь', )
    recipe = ForeignKey(Recipe,
                        on_delete=CASCADE,
                        related_name='purchases',
                        verbose_name='рецепт в покупках', )

    class Meta:
        unique_together = ['user', 'recipe']
        verbose_name = 'покупка'
        verbose_name_plural = 'покупки'
