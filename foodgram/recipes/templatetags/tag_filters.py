from django import template

register = template.Library()


@register.filter
def get_tags_from_request(request):
    return request.GET.getlist('tags')


@register.filter
def get_filter_link(request, tag):
    tags = request.GET.getlist('tags')
    if tag.slug in tags:
        tags.remove(tag.slug)
    else:
        tags.append(tag.slug)
    return '?tags=' + '&tags='.join(tags) if tags else '.'


@register.filter
def get_tags(get_params):
    tags = get_params.getlist("tags")
    if tags:
        result = "tags=" + "&tags=".join(tags)
        return result
