from rest_framework import serializers
from category.models import Category

# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
