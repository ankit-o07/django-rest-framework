from django.urls import path
from . import views  


urlpatterns=[
    path("", views.product_mixin_view), 
    # path("" ,  views.product_list_view),
    # path("" ,  views.product_create_view),
    path("<int:pk>/update/", views.product_update_view),
    
    path("<int:pk>/delete/", views.product_delete_view), 
    path("<int:pk>/", views.product_mixin_view), 
    # path("<int:pk>/", views.product_alt_view), 
    

]