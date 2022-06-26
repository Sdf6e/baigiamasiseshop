from django.db import models
from django.core.validators import MinValueValidator

class Product(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    inventory = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self) -> str:
        return self.title

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False, null=True, blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

class Address(models.Model):
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null= True)
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    zipcode = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address