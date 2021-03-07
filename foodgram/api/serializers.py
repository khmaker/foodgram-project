from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from recipes.models import Follow, Favorite, Purchase, Ingredient


class AuthorSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return self.Meta.model.objects.create(**validated_data)

    class Meta:
        model = None


class FollowSerializer(AuthorSerializer):

    def validate_author(self, author_id):
        user = self.context['request'].user
        if user.id == author_id:
            raise ValidationError('You can\'t follow yourself!')
        return author_id

    class Meta:
        fields = ['author', ]
        model = Follow


class FavoriteSerializer(AuthorSerializer):
    class Meta:
        fields = ['recipe', ]
        model = Favorite


class PurchaseSerializer(AuthorSerializer):
    class Meta:
        fields = ['recipe', ]
        model = Purchase


class IngredientSerializer(ModelSerializer):
    class Meta:
        fields = ['title', 'unit']
        model = Ingredient
