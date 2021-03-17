from django import forms
from django.core.exceptions import ObjectDoesNotExist

from recipes.models import AmountOfIngredient
from recipes.models import Ingredient
from recipes.models import Recipe


class RecipeForm(forms.ModelForm):

    def __init__(self, data=None, *args, **kwargs):
        self.ingredients = {}
        if data is not None:
            data = data.copy()
            self.get_ingredients(data)

        super().__init__(data=data, *args, **kwargs)

    def get_ingredients(self, data):
        for key, name in data.items():
            if key.startswith('nameIngredient'):
                _, _, number = key.partition('_')
                value = f'valueIngredient_{number}'
                self.ingredients[name] = {'amount': int(data.get(value))}

    def save(self, commit=True):
        recipe = super().save(commit=False)
        recipe.save()
        objects = []
        for data in self.ingredients.values():
            objects.append(AmountOfIngredient(recipe=recipe,
                                              ingredient=data.get('object'),
                                              amount=data.get('amount'), )
                           )
        if objects:
            recipe.amount.all().delete()
            AmountOfIngredient.objects.bulk_create(objects)
        self.save_m2m()
        return recipe

    def clean(self):
        if not self.ingredients:
            raise forms.ValidationError('Empty ingredients list not allowed')
        for title, amount in self.ingredients.items():
            if amount.get('amount') < 0:
                raise forms.ValidationError(f'Invalid value for {title}')
            try:
                ingredient = Ingredient.objects.filter(title=title).get()
                self.ingredients[title].update({'object': ingredient})
            except ObjectDoesNotExist:
                raise forms.ValidationError(f'{title} not valid ingredient')
        return super().clean()

    class Meta:
        model = Recipe
        fields = ('title',
                  'image',
                  'description',
                  'tags',
                  'cook_time',)
        widgets = {'tags': forms.CheckboxSelectMultiple(), }
