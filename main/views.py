from django.shortcuts import render,redirect
from .models import *
import datetime
import os
from django.http import StreamingHttpResponse
import mimetypes
from wsgiref.util import FileWrapper

# Create your views here.
def index(request):

    products=Products.objects.all()
    categories=Categories.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        mobile=request.POST.get('mob_number')
        email=request.POST.get('email')
        message=request.POST.get('message')
        sc, created = Contact.objects.get_or_create(created_at=datetime.datetime.now(), name=name, email=email,
                                                        number=mobile, message=message)
        sc.save()
    return render(request,'index.html',{'products':products,'categories':categories,'index':'active'})


def product_list(request,**kwargs):
    if 'category_pk' in kwargs:
        category=Categories.objects.get(pk=kwargs.get('category_pk'))
        products=Products.objects.filter(category=category)

    else:
        category={'title':"Printers",'description':''}
        products=Products.objects.all()

    return render(request,'products_list.html',{'products':products,'category':category})


def product(request,**kwargs):
    if 'prodpk' in kwargs:
        product=Products.objects.get(pk=kwargs.get('prodpk'))
    else:
        return redirect('index')
    if request.method=='POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mob_number')
        email = request.POST.get('email')
        sc, created = Contact.objects.get_or_create(created_at=datetime.datetime.now(), name=name, email=email,
                                                    number=mobile, message="Brochure Download")
        sc.save()

        filepath=product.brochure.path
        thefile=filepath

        chunk_size=8192
        response=StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),
                                       content_type=mimetypes.guess_type(thefile)[0])
        response['Content-Length']=os.path.getsize(thefile)
        response['Content-Disposition']="Attachment;filename=%s" % "Digital Innovations.pdf"
        return response

    return render(request,'product.html',{"product":product})

def contact_us(request):
    contact_us='active'
    return render(request,'contactus.html',{'contact_us':contact_us})


def about_us(request):
    about_us='active'
    return render(request,'about_us.html',{'about_us':about_us})

