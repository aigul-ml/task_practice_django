from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.title}"