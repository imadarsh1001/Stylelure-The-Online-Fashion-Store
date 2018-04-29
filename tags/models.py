from django.db import models

from Products.models import Product
# Create your models here.

class Tag(models.Model):
    products    = models.ManyToManyField(Product, blank=True)
    title       = models.CharField(max_length=120)
    slug        = models.SlugField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)

    def __str__(self):
        return self.title
