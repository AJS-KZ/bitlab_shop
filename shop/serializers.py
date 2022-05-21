from rest_framework import serializers

from shop.models import Products


class ProductsReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = "__all__"


class ProductsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("name", "price")
