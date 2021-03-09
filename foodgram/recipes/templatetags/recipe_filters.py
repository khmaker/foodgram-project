from django import template

register = template.Library()


@register.filter
def in_purchases(recipe_id, user):
    if user.is_authenticated:
        return user.purchases.filter(recipe=recipe_id).exists()


@register.filter
def is_favorite(recipe_id, user):
    if user.is_authenticated:
        result = user.favorites.filter(recipe=recipe_id).exists()
        return result


@register.filter
def ending(count):
    n = count % 10
    return ('ов' if n == 0 or 4 < n < 10 or 10 < n % 10 < 15
            else 'а' if 1 < n < 5 else '')
