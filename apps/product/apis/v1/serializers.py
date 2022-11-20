from rest_framework.serializers import ModelSerializer, ValidationError
from apps.product.models.category import Category
from apps.product.models.product import Product


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
        read_only = ('id',)


class ProductSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'price')
        read_only = ('id',)

    def validate(self, attrs):
        if not attrs.get('category'):
            raise ValidationError('Category must add !')
        return attrs
