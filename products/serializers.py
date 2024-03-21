# Serializer: Modelをどのようにシリアライズするかを決めるもの

from rest_framework import serializers

from .models import Family, Product, User


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['name']   # APIとして出力したいフィールド名

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'family']   # APIとして出力したいフィールド名

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'is_checked', 'price', 'family']

