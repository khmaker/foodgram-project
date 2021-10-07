# coding=utf-8
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    CurrentUserDefault, HiddenField,
    ModelSerializer,
)

from recipes.models import Favorite, Follow, Ingredient, Purchase


def validate_author(data):
    if data.get('author') == data.get('user'):
        raise ValidationError('You can\'t follow yourself!')
    return data


class FollowSerializer(CurrentUserDefault, ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ('author', 'user')
        model = Follow
        validators = (validate_author,)


class FavoriteSerializer(CurrentUserDefault, ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ('recipe', 'user')
        model = Favorite


class PurchaseSerializer(CurrentUserDefault, ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ('recipe', 'user')
        model = Purchase


class IngredientSerializer(ModelSerializer):
    class Meta:
        fields = ('title', 'unit')
        model = Ingredient
