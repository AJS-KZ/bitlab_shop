from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from shop.views import ProductsViewSet, home


router = DefaultRouter()

router.register('products', ProductsViewSet)


urlpatterns = [
    path('test123/', home)
] + router.urls
