from rest_framework import generics , mixins ,permissions , authentication
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializers
from api.permissions import IsStaffEditorPermission
from django.shortcuts import get_object_or_404


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
       
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get('content')
       
        if content is None :
            content = title
        serializer.save(content=content)
    

product_create_view = ProductCreateAPIView.as_view()


class ProductListCreateAPIView(
            generics.ListCreateAPIView,
            IsStaffEditorPermission,
            
            ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    # authentication_classes = [
    #     authentication.SessionAuthentication,
    #     TokenAuthentication,    
    # ]
    permission_classes = [permissions.IsAdminUser ,IsStaffEditorPermission]
    def perform_create(self, serializer):
        
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get('content') or None
        
        if content is None :
            content = title
        serializer.save(content=content)
    
product_list_create_view = ProductListCreateAPIView.as_view()










class ProductDetailAPIView(generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    
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

# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer = ProductSerializers
    
#     def post(self,request, *args,**kwargs):
#         return  self.list(request,*args,**kwargs)




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


class ProductMixinView(
                mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    def get(self , request, *args,**kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs) 
    
    def post(self , request ,*args, **kwargs):
        return self.create(request ,*args, **kwargs)
    

product_mixin_view = ProductMixinView.as_view()