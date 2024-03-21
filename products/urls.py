from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import FamilyViewSet, UserViewSet, ProductViewSet


router = DefaultRouter()
router.register('families', FamilyViewSet)
router.register('users', UserViewSet)
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
