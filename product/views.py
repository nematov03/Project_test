from django.shortcuts import render
from .models import Product
# Create your views here.

def Index(req):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(req,'index.html',context)

def DetailPage(req,pk):
    product = Product.objects.get(id=pk)
    return render(req,'detail.html',{'products':product})