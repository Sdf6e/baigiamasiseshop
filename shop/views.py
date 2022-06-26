from django.shortcuts import render
from .models import *


def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render (request, 'shop/shopmenu.html', context)

def cart(request):
    context = {}
    return render (request, 'shop/cartmenu.html')

def checkout(request):
    context = {}
    return render (request, 'shop/checkoutmenu.html')
    
