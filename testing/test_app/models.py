from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 200, null=True)
    email = models.CharField(max_length = 200, null=True)
    phone = models.CharField(max_length = 200, null=True)

    def __str__ (self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = 200, null=True)

    def __str__ (self):
        return self.name

class Product(models.Model):
    CATEGORY =  (
        ('new', 'new'),
        ('old' , 'old'),
        ('used', 'used')
    )
    
    name = models.CharField(max_length = 200, null=True)
    price = models.FloatField(max_length = 200, null=True)
    category = models.CharField(max_length = 200, null=True, choices = CATEGORY)
    decsription = models.CharField(max_length = 200, null=True, blank=True)
    tag = models.ManyToManyField(Tag, max_length = 200, null=True)

    def __str__ (self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('ordered' , 'ordered'),
        ('delivered' , 'delivered'),
        ('pending' , 'pending')
    )

    product = models.ForeignKey(Product, max_length = 200, null=True, on_delete = models.SET_NULL)
    customer = models.ForeignKey(Customer, max_length = 200, null=True, on_delete = models.SET_NULL)
    status = models.CharField(max_length = 200, null=True, choices = STATUS)

    def __str__ (self):
        return self.product.name

