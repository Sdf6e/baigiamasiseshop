from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)

class Adress(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)