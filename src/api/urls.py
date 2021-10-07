# coding=utf-8
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    FavoritesViewSet, FollowViewSet, IngredientViewSet,
    PurchaseViewSet,
)

router = DefaultRouter()
router.register(r'subscriptions', FollowViewSet, basename='subscriptions')
router.register(r'favorites', FavoritesViewSet, basename='favorites')
router.register(r'purchases', PurchaseViewSet, basename='purchases')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls)),
]
