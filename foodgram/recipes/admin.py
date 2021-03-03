from django.contrib import admin

from .models import Recipe, Tag, Ingredient, AmountOfIngredients

admin.site.register((Recipe, Tag, Ingredient, AmountOfIngredients))
