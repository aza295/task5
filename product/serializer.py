from rest_framework import  serializers
from rest_framework.generics import DestroyAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, CreateAPIView

from product.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


