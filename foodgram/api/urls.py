from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import FavoritesViewSet
from api.views import FollowViewSet
from api.views import IngredientViewSet
from api.views import PurchaseViewSet


router = DefaultRouter()
router.register(r'subscriptions', FollowViewSet, basename='subscriptions')
router.register(r'favorites', FavoritesViewSet, basename='favorites')
router.register(r'purchases', PurchaseViewSet, basename='purchases')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')

urlpatterns = [
    path('v1/', include(router.urls)),
]
