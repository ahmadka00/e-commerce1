from rest_framework import serliazer
from store.models import *

class CategorySerializers(serliazer.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serliazer.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'title', 'image', 'slug', 'price']