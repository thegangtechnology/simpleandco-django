from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=42)
    content = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    #  TODO : Implement this
    pass
