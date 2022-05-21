from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from shop.models import Products
from shop.serializers import ProductsReadSerializer, ProductsCreateSerializer


class ProductsViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsReadSerializer
    permission_classes = [AllowAny, ]
