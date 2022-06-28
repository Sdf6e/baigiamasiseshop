from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json


def shop(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, payment_status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_quantity':0 }
        cartItems = order['get_cart_quantity']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render (request, 'shop/shopmenu.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, payment_status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_quantity':0 }
        cartItems = order['get_cart_quantity']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render (request, 'shop/cartmenu.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, payment_status=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_quantity
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_quantity':0 }
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render (request, 'shop/checkoutmenu.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, payment_status=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity +1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity -1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)

def productdetail(request):
    return render(request, 'shop/detailmenu.html')
