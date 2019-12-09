"""mst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('index/',views.index,name="shopIndex"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('tracker/',views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
    path('prodView/<int:myid>',views.prodView,name="prodView"),
    path('checkout/',views.checkout,name="checkout"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('logout/',views.logout,name="logout"),
    path('userInfo_form/',views.userInfo_form,name="userInfo_form"),
    path('userInfo_list/',views.userInfo_list,name="userInfo_list"),
    path('delete_user_info/<int:uid>',views.delete_user_info,name="delete_user_info"),
    path('edit_user_info/<int:uid>',views.edit_user_info,name="edit_user_info"),
    path('update_user_info/<int:uid>',views.update_user_info,name="update_user_info"),
    path('add_product/',views.add_product,name="add_product"),
]
