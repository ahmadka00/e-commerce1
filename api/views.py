from store.models import Category, Product
from api.serializers import CategorySerializers, ProductSerializer
from django.http import Http404
from rest_framework import generics

class CategoryList(generics.ListCreateAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializers