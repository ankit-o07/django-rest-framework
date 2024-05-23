from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet , ProductGenericViewSet


router = DefaultRouter()
# router.register('product-abc',ProductViewSet,basename='products')
router.register('product-abc',ProductGenericViewSet,basename='products')
urlpatterns = router.urls

