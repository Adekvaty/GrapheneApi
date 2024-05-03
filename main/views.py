from django.shortcuts import render
from rest_framework import viewsets, permissions

from main.models import Brand, Clothes
from main.serializers import BrandSerializer, ClothesSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

    http_method_names = ['get', 'post', 'put', 'delete']
    lookup_field = 'id'
    lookup_url_kwarg = 'brand_id'

class ClothesViewSet(viewsets.ModelViewSet):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
    permission_classes = [permissions.IsAuthenticated]

    http_method_names = ['get', 'post', 'put', 'delete']
    lookup_field = 'id'
    lookup_url_kwarg = 'clothes_id'


