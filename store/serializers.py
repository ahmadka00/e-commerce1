from rest_framework import serializers
from store.models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ 'category', 'created_by','title', 'description', 'image', 
                  'slug', 'price', 'is_active', 'in_stock', 'created']
        
        # def create(self, validated_data):
        #     validated_data['created_by'] = self.context['request'].user
        #     return super().create(validated_data)
