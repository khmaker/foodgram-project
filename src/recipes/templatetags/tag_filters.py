# coding=utf-8
from django import template

register = template.Library()


@register.filter
def get_tags_from_request(request):
    return request.GET.getlist('tags')


@register.filter
def get_tag_filter(request, tag):
    tags = request.GET.getlist('tags')
    if tag.slug in tags:
        tags.remove(tag.slug)
    else:
        tags.append(tag.slug)
    return '?tags=' + '&tags='.join(tags) if tags else '.'


@register.filter
def get_tags_for_pagination(request):
    tags = request.GET.getlist('tags')
    return '&tags=' + '&tags='.join(tags) if tags else ''
