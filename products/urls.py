from rest_framework.routers import SimpleRouter
from products.views import ProductViewSet, CategoryViewSet

router = SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls
