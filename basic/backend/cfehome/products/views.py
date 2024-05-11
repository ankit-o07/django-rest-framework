from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get('content')
       
        if content is None :
            content = title
        serializer.save(content=content)
    

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    print(queryset)

    serializer_class = ProductSerializers
    print(serializer_class)
    

product_detail_view = ProductDetailAPIView.as_view()

