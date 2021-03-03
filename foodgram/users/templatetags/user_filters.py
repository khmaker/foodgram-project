from django import template

register = template.Library()


@register.filter
def add_class(field, css):
    return field.as_widget(attrs={'class': css})


@register.filter
def is_followed(author_id, user):
    result = user.follower.filter(author=author_id).exists()
    return result
