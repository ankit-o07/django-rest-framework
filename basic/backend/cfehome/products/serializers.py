from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse 
from .validators import unique_product_title , validate_title_no_hello
from api.serializers import UserPublicSerializer

class ProductSerializers(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    
    # my_user_data = serializers.SerializerMethodField(read_only= True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field="pk" )
    title = serializers.CharField(validators=[unique_product_title , validate_title_no_hello])
    body = serializers.CharField(source="content")
    # email = serializers.EmailField(source="user.email",read_only=True)

    class Meta:
        model = Product
        fields = [
            "user",
            'url', 
            'edit_url',
            'pk',
            'title',
            'body',
            'price',
            'sale_price',
            'public',
            'path',
            
           
        ]

    def get_my_user_data(self,obj):
        return {
            "username":obj.user.username
        }
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    
    # def update(self,instance , validated_data):
    #     email = validated_data.pop("email")
    #     return super().update(instance , validated_data)

    def get_edit_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
        
    
    def get_my_discount(self, obj):
        
        if not hasattr(obj,"id"):
            return None
        if not isinstance(obj,Product):
            return None
        
        return obj.get_discount()
    

   


















"""

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
                    view_name='product-detail',
                    lookup_field="pk"
                    )
    # email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            'url', 
            'edit_url',
            
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]

        
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value


    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    
    # def update(self,instance , validated_data):
    #     email = validated_data.pop("email")
    #     return super().update(instance , validated_data)

    def get_edit_url(self,obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
        
    
    def get_my_discount(self, obj):
        
        if not hasattr(obj,"id"):
            return None
        if not isinstance(obj,Product):
            return None
        
        return obj.get_discount()
    

"""
