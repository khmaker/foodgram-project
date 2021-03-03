from django import template

register = template.Library()


@register.filter
def in_purchases(recipe_id, session):
    recipes: list = session.get('shop_list')
    return recipes and recipe_id in recipes


@register.filter
def is_favorite(recipe_id, user):
    result = user.favorites.filter(recipe=recipe_id).exists()
    return result
