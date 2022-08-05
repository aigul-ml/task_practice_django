from django.db import models

from django.contrib.auth import get_user_model

from product.models import Product


User = get_user_model()

class Review(models.Model):
    author = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete =models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])

    def __str__(self):
        return f"{self.author} -> {self.product}"