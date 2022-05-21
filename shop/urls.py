from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from shop.views import ProductsViewSet


router = DefaultRouter()

router.register('products', ProductsViewSet)


urlpatterns = [
] + router.urls
