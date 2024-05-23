from rest_framework import viewsets , mixins

from .models import Product
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"


class ProductGenericViewSet(
        viewsets.GenericViewSet,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin
        ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"


# product_list_view = ProductGenericViewSet.as_view({'get':'list'})

# product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})
