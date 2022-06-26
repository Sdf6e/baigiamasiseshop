from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.views import generic

def shop(request):
    context = {}
    return render (request, 'shop/shopmenu.html')

def cart(request):
    context = {}
    return render (request, 'shop/cartmenu.html')

def checkout(request):
    context = {}
    return render (request, 'shop/checkoutmenu.html')
    
