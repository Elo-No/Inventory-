from rest_framework.generics import CreateAPIView, ListAPIView

from apps.core.permissions import IsSellerOrAdminOrReadOnly, IsAdminOrReadOnly
from apps.product.apis.v1.serializers import ProductSerializer, CategorySerializer
from apps.product.models.product import Product


class CreateProductAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsSellerOrAdminOrReadOnly]


class ListProductAPIView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsSellerOrAdminOrReadOnly]

    def get_queryset(self):
        return Product.objects.all()


class CreateCategoryAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
