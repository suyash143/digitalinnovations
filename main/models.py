from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='static/product')


class Products(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True,upload_to='static/product')
    brochure=models.FileField(blank=True,null=True)
    category=models.ForeignKey(Categories,on_delete=models.SET_NULL,null=True,blank=True)


class Contact(models.Model):
    name=models.CharField(max_length=500,null=True,blank=True)
    number=models.IntegerField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(null=True,blank=True,auto_now_add=True)
    status=models.CharField(max_length=100,null=True,blank=True)
