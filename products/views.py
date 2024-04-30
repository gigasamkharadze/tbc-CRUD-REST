from rest_framework.viewsets import ModelViewSet
from products.models import Product, Category
from products.serializers import ProductListSerializer, ProductDetailSerializer, ProductUpdateSerializer
from products.serializers import CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'update':
            return ProductUpdateSerializer
        return ProductDetailSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
