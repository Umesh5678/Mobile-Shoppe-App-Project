"""College URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from College1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about),
    path('contact/',views.contact),
    path('save_response/',views.save_response),
    path('login/',views.login),
    path('cart/',views.cart),
    # path('delete_item',views.delete_item),
    path('logout/',views.delete_session),
    path('dologin/',views.dologin),
    path('signup',views.signup),
    path('signup_form/',views.signup_Form),
    path('shopall/',views.shopall),
    path('mobile/',views.mobile),
    path('tablet/',views.tablet),
    path('accessories/',views.accessories),
    path('product_details/',views.product_details),
    path('chat_msg/',views.chat_msg)
    
    
    
    
 
    
   
    
    
    
]
