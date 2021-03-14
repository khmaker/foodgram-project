from django.contrib import admin

from recipes.models import AmountOfIngredient
from recipes.models import Favorite
from recipes.models import Follow
from recipes.models import Ingredient
from recipes.models import Purchase
from recipes.models import Recipe
from recipes.models import Tag


class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'author',)


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'unit',)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

admin.site.register((Tag, Follow, Favorite, Purchase, AmountOfIngredient))
