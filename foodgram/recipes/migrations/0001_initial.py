import django.db.models.deletion
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ]

    operations = [
        migrations.CreateModel(
            name='AmountOfIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(
                    verbose_name='количество ингредиента')),
                ],
            options={
                'verbose_name': 'количество ингредиентов',
                },
            ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True,
                                           verbose_name='название '
                                                        'ингредиента')),
                ('unit', models.CharField(max_length=64,
                                          verbose_name='единица измерения')),
                ],
            options={
                'verbose_name': 'ингредиент',
                'verbose_name_plural': 'ингредиенты',
                'ordering': ['title'],
                },
            ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title',
                 models.CharField(max_length=100, verbose_name='имя тега')),
                ('slug', models.SlugField(unique=True)),
                ('color', models.CharField(
                    choices=[('green', 'Green'), ('orange', 'Orange'),
                             ('purple', 'Purple')], default='green',
                    max_length=30)),
                ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
                },
            ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200,
                                           verbose_name='название рецепта')),
                ('image', models.ImageField(blank=True,
                                            help_text='Здесь можно загрузить'
                                                      ' картинку',
                                            null=True,
                                            upload_to='recipe_pics/',
                                            verbose_name='загрузить '
                                                         'картинку')),
                ('description', models.TextField(verbose_name='описание')),
                ('cook_time', models.PositiveSmallIntegerField(
                    verbose_name='время приготовления')),
                ('pub_date',
                 models.DateTimeField(auto_now_add=True, db_index=True,
                                      verbose_name='дата публикации')),
                ('slug',
                 models.SlugField(default=None, max_length=100, null=True,
                                  unique=True,
                                  verbose_name='уникальная часть URL для '
                                               'рецепта')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='recipes',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='автор')),
                ('ingredients',
                 models.ManyToManyField(related_name='recipe_ingredient',
                                        through='recipes.AmountOfIngredient',
                                        to='recipes.Ingredient',
                                        verbose_name='ингредиенты')),
                ('tags', models.ManyToManyField(related_name='recipes',
                                                to='recipes.Tag',
                                                verbose_name='теги')),
                ],
            options={
                'verbose_name': 'рецепт',
                'verbose_name_plural': 'рецепты',
                'ordering': ['-pub_date', 'title'],
                },
            ),
        migrations.AddField(
            model_name='amountofingredient',
            name='ingredient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='amount', to='recipes.ingredient'),
            ),
        migrations.AddField(
            model_name='amountofingredient',
            name='recipe',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='amount', to='recipes.recipe'),
            ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('recipe',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='purchases',
                                   to='recipes.recipe',
                                   verbose_name='рецепт в покупках')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='purchases',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='пользователь')),
                ],
            options={
                'verbose_name': 'покупка',
                'verbose_name_plural': 'покупки',
                'unique_together': {('user', 'recipe')},
                },
            ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='following',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Подписки')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='follower',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='Подписчик')),
                ],
            options={
                'verbose_name': 'подписка',
                'verbose_name_plural': 'подписки',
                'unique_together': {('user', 'author')},
                },
            ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('recipe',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='favorites',
                                   to='recipes.recipe')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='favorites',
                                   to=settings.AUTH_USER_MODEL)),
                ],
            options={
                'verbose_name': 'избранное',
                'unique_together': {('user', 'recipe')},
                },
            ),
        migrations.AlterUniqueTogether(
            name='amountofingredient',
            unique_together={('recipe', 'ingredient')},
            ),
        ]
