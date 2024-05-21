from django.urls import path , include
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns=[
    path("auth/",obtain_auth_token),
    path("",views.api_home),

    
]