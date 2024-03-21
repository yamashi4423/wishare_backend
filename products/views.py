# ViewSet: APIのクエリーをどう解釈するかを決めるもの

from django.shortcuts import render
from rest_framework import filters, viewsets

from .models import Family, Product, User
from .serializers import FamilySerializer, ProductSerializer, UserSerializer


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer