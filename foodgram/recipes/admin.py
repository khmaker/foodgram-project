from django.contrib import admin

from .models import (Recipe, Tag, Ingredient, AmountOfIngredient,
                     Follow, Favorite, Purchase,
                     )


class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'author', )


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'unit', )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)

admin.site.register((Tag, Follow, Favorite, Purchase, AmountOfIngredient))
