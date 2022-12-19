from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    products=Products.objects.all()
    categories=Categories.objects.all()
    return render(request,'index.html',{'products':products,'categories':categories})


def product_list(request):

    return render(request,'products_list.html')