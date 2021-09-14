from recipes.models import Ingredient


def add_ingredients():
    create = Ingredient.objects.get_or_create
    with open('ingredients.csv', 'r', encoding='utf-8') as file:
        for i in file:
            title, _, unit = i.strip().rpartition(',')
            try:
                ingredient, created = create(title=title,
                                             unit=unit)
                if created:
                    ingredient.save()
            except Exception as e:
                print(e)
