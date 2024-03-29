from rest_framework import filters
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from recipes.models import Favorite
from recipes.models import Follow
from recipes.models import Ingredient
from api.serializers import FavoriteSerializer
from api.serializers import FollowSerializer
from api.serializers import IngredientSerializer
from api.serializers import PurchaseSerializer


class CreateDestroyViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        success = instance.delete()
        return Response({'success': bool(success)}, status=status.HTTP_200_OK)


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


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('$title',)
