from itertools import product
from django.db import models

class Citi(models.Model):
    cities = models.CharField(max_length=30)

    def __str__(self):
        return self.cities


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Supplier(models.Model):
    citi = models.OneToOneField(Citi, on_delete = models.CASCADE, primary_key = True)
    name_supplier = models.CharField(max_length=20)
    

    def __str__(self):
        return (self.citi, self.name_supplier)


class Сlient(models.Model):
    name_client = models.CharField(max_length=100)
    citi = models.ForeignKey(Citi,on_delete = models.CASCADE, primary_key = True)
    product = models.ManyToManyField(Product)
    
    class Meta:
        ordering = ['name_client', 'citi']
    
    def __str__(self):
        return self.name_client