# store/models.py
from django.db import models

class Rice(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='rice_images/', blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    rice = models.ForeignKey(Rice, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    session_key = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.quantity} of {self.rice.name}"

    @property
    def total_price(self):
        return self.quantity * self.rice.price


class Order(models.Model):
    name = models.CharField(max_length=100)
    rice = models.ForeignKey('Rice', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    created_at = models.DateField(auto_now_add=True)  # Ensure this is a DateField

    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.rice.name}"
    
class CartItem(models.Model):
    rice = models.ForeignKey(Rice, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.rice.price
