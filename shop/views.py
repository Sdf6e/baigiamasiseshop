from django.shortcuts import render
from .models import *


def shop(request):
    products = Product.objects.all()
    context = {'products':products}
    return render (request, 'shop/shopmenu.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, payment_status=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items':items}
    return render (request, 'shop/cartmenu.html', context)

def checkout(request):
    context = {}
    return render (request, 'shop/checkoutmenu.html')
    
