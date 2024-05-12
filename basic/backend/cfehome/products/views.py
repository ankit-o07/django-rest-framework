from django.shortcuts import render
from rest_framework import generics
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializers
from rest_framework.decorators import api_view
from django.http import Http404
from django.shortcuts import get_object_or_404

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get('content')
       
        if content is None :
            content = title
        serializer.save(content=content)
    

product_create_view = ProductCreateAPIView.as_view()


class ProductListCreateAPIView(generics.ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get('content')
       
        if content is None :
            content = title
        serializer.save(content=content)
    
product_list_view = ProductListCreateAPIView.as_view()










class ProductDetailAPIView(generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
    


    def perform_update(self, serializer):
        print("test ")
        instance = serializer.save() 
        if not instance.content :
            instance.content = instance.title    
    
product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
    


    def perform_destroy(self,instance):
        super().perform_destroy(instance)
        
    
product_delete_view = ProductDeleteAPIView.as_view()

   


@api_view(['GET','POST'])
def  product_alt_view(request,pk=None ,*arg, **kwargs):
    method = request.method
    
    if method == "GET":
        if pk is not None :
            obj = get_object_or_404(Product ,  pk= pk )
            data = ProductSerializers(obj, many =False).data
            return Response(data)
        
        # if pk is not None:
        #     # detail view
        #     queryset = Product.objects.filter(pk=pk)
        #     if not queryset.exists():
        #         raise Http404
            
        
        queryset = Product.objects.all()
        data = ProductSerializers(queryset , many=True).data
        
        print(ProductSerializers(queryset , many=True))
       
        
        return Response(data)


    if method == "POST":
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get('content')
       
            if content is None :
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        
        return Response({"invalid":"not good data"}, status=400)
