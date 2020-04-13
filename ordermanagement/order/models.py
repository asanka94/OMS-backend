from django.db import models
from ordermanagement.product.models import Product
from ordermanagement.accounts.models import User


class Order(models.Model):
    name = models.CharField(max_length=100)
    total = models.TextField()
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

