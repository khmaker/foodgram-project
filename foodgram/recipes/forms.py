from django import forms

from .models import Recipe, AmountOfIngredients, Ingredient


class RecipeForm(forms.ModelForm):

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            self.ingredients = self.get_ingredients(data)

        super().__init__(data=data, *args, **kwargs)

    @staticmethod
    def get_ingredients(data):
        ingredients = {}
        for key, name in data.items():
            if key.startswith('nameIngredient'):
                number = key.split('_')[1]
                value = f'valueIngredient_{number}'
                ingredients[name] = data.get(value)

        return ingredients

    def save(self, commit=True):
        recipe = super().save(commit=False)
        recipe.save()
        objects = []
        for title, amount in self.ingredients.items():
            ingredient = Ingredient.objects.filter(title=title)
            if ingredient.exists():
                objects.append(AmountOfIngredients(recipe=recipe,
                                                   ingredient=ingredient.get(),
                                                   amount=int(amount), )
                               )

        recipe.amount.all().delete()
        AmountOfIngredients.objects.bulk_create(objects)
        self.save_m2m()
        return recipe

    def clean(self):
        for title, amount in self.ingredients.items():
            ingredient = Ingredient.objects.filter(title=title)
            if not ingredient.exists():
                raise forms.ValidationError(f'{title} not valid ingredient')
        return super().clean()

    class Meta:
        model = Recipe
        fields = ('title',
                  'image',
                  'description',
                  'tags',
                  'cook_time', )
        widgets = {'tags': forms.CheckboxSelectMultiple(), }
