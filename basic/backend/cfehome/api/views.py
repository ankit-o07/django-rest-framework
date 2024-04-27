import json
from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import PrimaryProductSerializers , SecondaryProductSerializers , ProductSerializers



@api_view(['POST'])
def api_home(request, *args,**kwargs ): 
    data ={}
    
    # instance = Product.objects.all().order_by("?").first()
    # data = {}

    # if instance:
    #     # data = model_to_dict(model_data, fields=['title', 'id','price', "sale_price" ])
    #     data = ProductSerializers(instance).data
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
        
    return Response({"invalid":"not good data"}, status=400)




"""
@api_view(["GET"])
def api_home(request, *args,**kwargs ): 

    
    model_data = Product.objects.all().order_by("?").first()
    data = {}

    if model_data:
        data = model_to_dict(model_data, fields=['title', 'id','price', "sale_price" ])
    return Response(data)
"""
#-----------------------------------break Point
        # data['title'] = model_data.title
        # data['cotent'] = model_data.content
        # data['price'] = model_data.price
        # data["ID"]  = model_data.id

    #     """
    #         model instance (Model_data)
    #         turn  python dict 
    #         return JSON to my client
    #     """

    #     json_dat_str = json.dumps(data)
    # return HttpResponse(json_dat_str,headers={"cotent-type":"application/json"})
    
    

# def api_home(request, *args,**kwargs ): 
#     print(request.GET)
#     body = request.body 
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
    
#     print("\n")
#     print("body")
#     print(data)
#     print("\n")
    
    
#     data['headers'] = json.dumps(dict(request.headers))
    
#     print(data['headers'])   
    
    
#     data['content_type'] = request.content_type
    
#     print(data.keys)  
    

#     return JsonResponse(data)
#     return JsonResponse({"message":"Hi there, this is your Django API respones!!"})
