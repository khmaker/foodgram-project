from django.contrib import admin

from .models import Recipe, Tag, Ingredient, AmountOfIngredients, Follow

admin.site.register((Recipe, Tag, Ingredient, AmountOfIngredients, Follow))
