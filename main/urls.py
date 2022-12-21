from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('product',views.product_list,name='product_list'),
    path('products/<int:category_pk>',views.product_list,name='product_list'),
    path('products/<str:category>/<str:title>',views.product_list,name='product_list'),
    path('product/<int:prodpk>',views.product,name='product'),
]