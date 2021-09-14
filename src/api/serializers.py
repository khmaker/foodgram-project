from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CurrentUserDefault
from rest_framework.serializers import HiddenField

from recipes.models import Favorite
from recipes.models import Follow
from recipes.models import Ingredient
from recipes.models import Purchase


def validate_author(data):
    if data.get('author') == data.get('user'):
        raise ValidationError('You can\'t follow yourself!')
    return data


class FollowSerializer(CurrentUserDefault, ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        fields = ('author', 'user')
        model = Follow
        validators = (validate_author, )


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
