# coding=utf-8
from rest_framework.filters import SearchFilter
from rest_framework.mixins import (
    CreateModelMixin, DestroyModelMixin,
    ListModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet

from api.serializers import (
    FavoriteSerializer, FollowSerializer,
    IngredientSerializer, PurchaseSerializer,
)
from recipes.models import Favorite, Follow, Ingredient


class CreateDestroyViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        success = instance.delete()
        return Response({'success': bool(success)}, status=HTTP_200_OK)


class FollowViewSet(CreateDestroyViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'author'


class FavoritesViewSet(CreateDestroyViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'recipe'


class PurchaseViewSet(CreateDestroyViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'recipe'

    def get_queryset(self):
        return self.request.user.purchases.all()


class IngredientViewSet(ListModelMixin, GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('$title',)
